"""
Student-side helpers for the WS1 ascii-art elimination game. Provided
code -- import and use show_round()/submit() as-is, nothing here is
meant to be read or edited by students.

BASE_URL is localhost, not the VM's public IP or domain: this code
runs INSIDE a student's own Hub-spawned kernel, which is a process on
the same VM as tier3-hub-service, same reasoning the service's own
HUB_URL (not HUB_PUBLIC_URL) uses "localhost" server-side.

Needs the `requests` package in TLJH's shared environment -- not
confirmed present yet (nbgitpuller itself needed a manual
`sudo /opt/tljh/user/bin/pip install` the first time it was used here,
per tier-3-plan.txt Phase 3 -- requests may need the same treatment,
untested).
"""

import contextlib
import io
import os

import requests
from IPython.display import HTML, Image, display

BASE_URL = "http://localhost:8000"

_session_code: str | None = None


def _code() -> str:
    global _session_code
    if _session_code is None:
        _session_code = input("Enter the session code: ").strip()
    return _session_code


def _hub_username() -> str:
    # Set by JupyterHub itself in every spawned server's environment --
    # the student never types or sees this, it's just how the system
    # already knows who's who (same identifier used throughout the
    # service's own progress tracking).
    return os.environ["JUPYTERHUB_USER"]


def show_round() -> None:
    """Run this once per round to reveal the current level's image."""
    resp = requests.get(f"{BASE_URL}/sessions/{_code()}/round/current/image")
    if resp.status_code == 404:
        print("Round hasn't started yet -- wait for the instructor, then run this again.")
        return
    resp.raise_for_status()
    display(Image(resp.content))


class submit:
    """
    with submit(level=1):
        print("Engineering")
        print("\\tis")
        print("\\t\\tAwesome")

    Captures what you print inside the block -- it won't show up live,
    everything you printed gets echoed back below, annotated line by
    line, once the block finishes. Run this cell again (your print()
    calls, not the round-reveal cell) as many times as you want to
    retry before time runs out.
    """

    def __init__(self, level: int):
        self.level = level
        self._buffer = io.StringIO()
        self._redirect = contextlib.redirect_stdout(self._buffer)

    def __enter__(self) -> "submit":
        self._redirect.__enter__()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        self._redirect.__exit__(exc_type, exc_val, exc_tb)
        if exc_type is not None:
            # A real error in the student's own code -- let it surface
            # normally rather than silently swallowing it as "wrong
            # answer."
            return False

        lines = self._buffer.getvalue().split("\n")
        if lines and lines[-1] == "":
            lines.pop()

        resp = requests.post(
            f"{BASE_URL}/sessions/{_code()}/submit",
            json={"hub_username": _hub_username(), "level_number": self.level, "lines": lines},
        )
        resp.raise_for_status()
        result = resp.json()

        rows = []
        for line in result["lines"]:
            color = "#0EA5A0" if line["correct"] else "#D1483F"
            marker = "" if line["correct"] else "  &lt;-- wrong"
            shown = line["actual"] if line["actual"] is not None else "(nothing printed)"
            rows.append(
                f'<div style="color:{color};font-family:monospace">{shown}{marker}</div>'
            )

        verdict = "Correct!" if result["pass"] else "Not quite -- check the lines marked wrong."
        display(
            HTML(
                f'<div>{"".join(rows)}</div>'
                f'<p><b>{verdict}</b> Lives remaining: {result["lives_remaining"]}</p>'
            )
        )
        return True
