'''
for loops iterate through an iterable
format: for [variable-name] in [iterable]
some examples of iterables:
    range (a range of values)
    a list
    a dictionary's keys
    a set
    in short, anything made up of one or more values
'''

'''
let's take a look at the most common iterable used with a for loop: range
range() creates a group of integers values
for example, range(10) represents (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
for i in range(10):
    # i = 0, then 1, then 2, then 3... 9
here, i is the variable name and is how we access the range value

range can be called in the following ways:
    range(stop)
    range(start, stop)
    range(start, stop, step)
    default parameters: start = 0, step = 1
start value is included but stop is not
range(stop) starts at 0 and ends at stop - 1 with a step of 1
range(10) is the same thing as range(0, 10, 1)


examples:
0 to 100: range(100) or range(0, 100, 1)
1 to 99: range(1, 100, 1)


we can also use step parameter to specify how big of a jump
for example, if we want multiples of 3 to 100, our first multiple is 3 and we want every 3 numbers afterwards
hence, range(3, 101, 3)
'''

# sum of the first 100 numbers
total = 0
for i in range(101):
    total += i
print(total)

# sum of first 100 negative numbers
total2 = 0
for i in range(-1, -101, -1):
    total2 += i
print(total2)

# sum of even numbers up to 100:
total3 = 0
for i in range(1, 101, 2):
    total3 += i
print(total3)
