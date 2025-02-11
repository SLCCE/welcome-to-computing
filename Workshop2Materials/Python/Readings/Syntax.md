General note:
Python doesn't have braces for functions/loops/conditionals and instead has indentation

Variables
x = 1
x = 1.5
x = True

Strings
x = "Hi!"
x = "Hi!\n" -- \n is the newline character

Lists
a = [1, 2, 3, 4, 5]
one = a[0]
five = a[4]
fiveAlso = a[-1] -- gets the last item in a list
a.append(6) -- adds an element to the end of a list | a = [1, 2, 3, 4, 5, 6]
a.pop() -- removes the last element in a list

2 ways to loop through a list -- by index or by item
for i in range(len(a)):
    item = a[i]
    print(item)
for item in a:
    print(item)

Tuples
similar to a list but they can't be modified
t = (1, 2, 3)
one = t[0]
two = t[1]
three = t[2]

Conditionals
x = 3
if x == 1:
    print("x is 1")
elif x > 1 and x < 10:
    print("x is strictly between 1 and 10")
else:
    print("x is greater than or equal to 10")

Dictionary
maps a key to a value
You can imagine a list as a dictionary that maps 0 to the first element, 1 to the second element, and so on
It supports multiple types:
d = dict()
d['a'] = 1
d[0] = 2
d['favorite color'] = 'green'
d[True] = 3
Contents of d:
{
    'a': 1,
    0: 2,
    'favorite color': green, 
    True: 3
}
