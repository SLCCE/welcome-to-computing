y = 2
def f():
    global y
    print(y)
    y += 2
    
f()
print(y)
