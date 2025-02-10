'''
the most commonly used loop control statements are break and continue

break: break out of the current loop
continue: continue to the next iteration
let's take a look at these keywords in action
'''

n = 5
# stop when n reaches 10
while True:
    n += 1
    if n >= 10:
        break
print(n)

# equivalent to
n = 5
while n < 10: # note: if we have <=, 10 <= 10 is true and n becomes 11
    n += 1
print(n)

# print the even numbers from 1 to 10
x = 0
while x <= 10:
    x += 1
    # if x is odd, continue to the next iteration
    if x % 2 == 1:
        continue
    print(x)
