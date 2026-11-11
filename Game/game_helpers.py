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
        # Echoed back as a real printed line, not just input()'s own
        # transient prompt -- this becomes part of the cell's saved
        # output, so a student can scroll up and check it later (or
        # after a kernel restart, before this cache resets) without
        # needing to remember it or ask again.
        print(f"Using session code: {_session_code}")
    return _session_code


def enter_code() -> None:
    """
    Run this first, before anything else -- enter the session code
    your instructor gives you. Separate, explicit step (rather than
    leaving this as a side effect of the first show_round()/submit()
    call) so it's an obvious, documented part of getting started, not
    something that only incidentally happens.
    """
    _code()


def _hub_username() -> str:
    # Set by JupyterHub itself in every spawned server's environment --
    # the student never types or sees this, it's just how the system
    # already knows who's who (same identifier used throughout the
    # service's own progress tracking).
    return os.environ["JUPYTERHUB_USER"]


def _handle_error(resp: "requests.Response") -> str:
    """
    Returns a human-readable message for a failed request. Also resets
    the cached session code specifically when the failure means "that
    code doesn't correspond to any active session" -- every OTHER 404
    here (e.g. "no round active yet") is NOT a code problem and must
    NOT reset it, or a student would get re-prompted every single time
    they check before the instructor's actually started a round.
    """
    global _session_code
    try:
        detail = resp.json().get("detail", "Something went wrong.")
    except ValueError:
        return "Something went wrong talking to the game server."

    if isinstance(detail, dict):
        if detail.get("error") == "session_not_found":
            _session_code = None
        return detail.get("message", "Something went wrong.")
    return detail


def show_round() -> None:
    """Run this once per round to reveal the current level's image."""
    try:
        resp = requests.get(f"{BASE_URL}/sessions/{_code()}/round/current/image")
    except requests.RequestException:
        print("Couldn't reach the game server -- check with your instructor.")
        return
    if not resp.ok:
        # Uses the server's own message rather than a single hardcoded
        # guess -- "no round active yet" and "session not found" (e.g.
        # a mistyped code) are both 404s, and need different advice.
        print(_handle_error(resp))
        return
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

        try:
            resp = requests.post(
                f"{BASE_URL}/sessions/{_code()}/submit",
                json={"hub_username": _hub_username(), "level_number": self.level, "lines": lines},
            )
        except requests.RequestException:
            print("Couldn't reach the game server -- check with your instructor.")
            return True
        if not resp.ok:
            # E.g. submitting before the instructor's actually started
            # this round -- a real, likely mistake, not worth a raw
            # traceback over.
            print(_handle_error(resp))
            return True
        result = resp.json()

        rows = []
        for line in result["lines"]:
            color = "#0EA5A0" if line["correct"] else "#D1483F"
            marker = "" if line["correct"] else "  &lt;-- wrong"
            shown = line["actual"] if line["actual"] is not None else "(nothing printed)"
            rows.append(
                f'<div style="color:{color};font-family:monospace">{shown}{marker}</div>'
            )

        if result["already_secured"]:
            # Passed on an earlier attempt this round -- that's locked
            # in regardless of what this particular resubmission looks
            # like, so this must never read as a "wrong" verdict.
            verdict = "Already correct from an earlier attempt -- you're safe regardless of this one."
        elif result["pass"]:
            verdict = "Correct!"
        else:
            verdict = "Not quite -- check the lines marked wrong."

        display(
            HTML(
                f'<div>{"".join(rows)}</div>'
                f'<p><b>{verdict}</b> Lives remaining: {result["lives_remaining"]}</p>'
            )
        )
        return True


def display_score() -> None:
    """
    Run this once at the very end, after your instructor says the game
    is over -- NOT tied to whether your last submission happened to be
    correct or for the last level specifically. Checks the real
    end-of-game state on the server (has the final round actually
    resolved, do you still have lives left), so a wrong final attempt
    can't hide a win you already earned by surviving earlier rounds.
    """
    try:
        resp = requests.get(
            f"{BASE_URL}/sessions/{_code()}/game/score",
            params={"hub_username": _hub_username()},
        )
    except requests.RequestException:
        print("Couldn't reach the game server -- check with your instructor.")
        return
    if not resp.ok:
        print(_handle_error(resp))
        return
    result = resp.json()

    if not result["game_over"]:
        print("The game isn't over yet -- wait for the instructor to finish the last round.")
        return

    if result["won"]:
        display(
            HTML(
                '<p style="font-size:24px"><b>You win!</b></p>'
                f'<p>Lives remaining: {result["lives_remaining"]}</p>'
            )
        )
    else:
        display(
            HTML(f'<p><b>Game over</b> -- eliminated at level {result["eliminated_at_level"]}.</p>')
        )
