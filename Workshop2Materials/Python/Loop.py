# Intro to Loops
val = 0
# val starts at 0
print(val)
# Hi! I'm a loop. I'm useful for repeating operations
while val < 10:
    val += 1
# through the loop, val becomes: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
print(val)

# For example, a task that would be very time-consuming to find by hand
# Adding all integers from 1 to 100
total = 0
val = 0
while val < 100:
    # add 1, add 2, add 3... add 100
    total += val
# 5050
print(total)


# Same task but with a for loop
total = 0
for i in range(1, 101):
    total += i
print(total)
