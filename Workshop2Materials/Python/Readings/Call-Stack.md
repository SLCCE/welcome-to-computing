The call stack is how a program tracks what's being called.
It's named after the stack data structure.

For example, if I were to add the numbers 1, 2, and 3 to the stack:
add 1
top [1] bottom
add 2
top [2, 1] bottom
add 3
top [3, 2, 1] bottom

Now, to remove the elements:
pop()
top [2, 1] bottom
pop()
top [1] bottom
pop()
top [] bottom
^^ stack is now empty


Let's see how this applies to function calls:
def a():
    b()

def b():
    print("Hello World!")
a()

First, a gets called
top [a] bottom
Then, b gets called
top [b, a] bottom
Then, print gets called
top [print, b, a] bottom

print finishes running and we go back to b
top [b, a] bottom
b finishes running and we go back to a
top [a] bottom
a finishes running
top [] bottom

