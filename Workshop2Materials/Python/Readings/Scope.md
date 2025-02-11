A variable's scope is based on where it is declared and determines where it can be accessed. 

The first scope we'll take a look at is global.
A variable has global scope if it's declared on the top level and can be accessed anywhere. 

x = 5
def f():
    We can access x here because it has global scope
    print(x)
The above will print out 5


The other scope is local scope. 
def f():
    y = 2
    We can access y here because we're in its scope. 
    However, when we exit the function we can no longer access it. 
    print(y)
print(y) will produce an error here because y is local to the function f. 


An example of both scopes in action:
y = 2
def f(x):
    print(x) -- prints 'hi' (passed in as a parameter, also a local variable)
    print(y) -- prints 2 (global variable)
    z = 3
    print(z) -- prints 3 (local variable created inside the function)

f('hi')
print(x) -- error because x is a local variable inside the function
print(y) -- prints 2
print(z) -- error because z is a local variable inside the function



Something to note is if two variables of different scopes have the same name, 
getting the variable will access the one with the narrower scope
x = 2
def f(x):
    print(x) -- prints 'hi' since it has the narrower, more specific scope
f('hi')
print(x) -- prints 2, our global variable
