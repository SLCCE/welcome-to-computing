'''
While loops run while their condition is true
this condition is checked:
    * the first time
    * every time the code under the loop finishes running

Structure:
while [condition]:
    run until condition is false
'''

# a while loop will never be accessed if its condition is initially false
x = 0
while x != 0:
    print("Never accessed")

# also have to be careful to make sure that the condition eventually becomes false
# otherwise the code will run forever (See While-Forever.py)


x = 2
while x >= 0:
    print(x)
    x -= 1
# x hits 0, x >= 0 evaluates to True so the loop runs 1 more time, making x equal -1 in the end
print(x)


