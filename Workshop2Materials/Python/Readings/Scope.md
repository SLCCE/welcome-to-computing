# Python Scope

A variable's scope is based on where it is declared and determines where it can be accessed. The first scope we'll take a look at is global. A variable has global scope if it's declared on the top level and can be accessed anywhere.

```python
x = 5
def f():
    # We can access x here because it has global scope
    print(x)
f()
# The above will print out 5
```

The other scope is local scope.

```python
def f():
    y = 2
    # We can access y here because we're in its scope. 
    # However, when we exit the function we can no longer access it. 
    print(y)

# print(y) at this location will produce an error because y is local to the function f. 
```

An example of both scopes in action:

```python
y = 2
def f(x):
    print(x) # prints 'hi' (passed in as a parameter, also a local variable)
    print(y) # prints 2 (global variable)
    z = 3
    print(z) # prints 3 (local variable created inside the function)
f('hi')

# print(x) -- error because x is a local variable inside the function
print(y) -- prints 2
# print(z) -- error because z is a local variable inside the function

# Note: If we passed y into the function, ex. f(y), we could still print out y at the end because it has global scope. 
```

Since y is an integer and integers are immutable, if we wanted to modify y within the function, we'd need the global keyword. However, if y was a mutable object like a list, we would not need the global keyword.

Immutable: not able to be changed -- when we 'change' an immutable object, the program is actually replacing the instance of that object with separate one.

```python
y = 2
def f():
    global y
    print(y) # prints 2
    y += 2
    
f()
print(y) # prints 4
```

Example with mutable object: list.

```python
a = [1, 2, 3, 4, 5]
def f():
    # no global keyword needed here
    a[0] = 2
print(a) # [2, 2, 3, 4, 5]
```

Something to note is if two variables of different scopes have the same name, getting the variable will access the one with the narrower scope

```python
x = 2
def f(x):
    print(x) # prints 'hi' since it has the narrower, more specific scope
f('hi')
print(x) # prints 2, our global variable
```
