***Make a copy of the Python.py starter code. Fill out each section as you read this page.***

A **variable** is like a container that holds a value. You can think of it as a label for something you want to store. For example, you might want to store a number or a word and use it later in your program.

Let’s start with a variable that stores a number. In this case, we’re going to store the number 30 in a variable called favNumber. 

We do this with:

```py
favNumber = 30
```

Once we’ve stored a value in a variable, we can use the print() function to display it. Let’s print the value of favNumber:

```py
favNumber = 30

print(favNumber)
# Outputs 30
```

We can also ask the user to type in information and store their answer in a variable. To do this, we use the **input()** function.

For example, let’s ask the user for their favorite number:

```py
# Ask favorite number
favNumber = input("What is your favorite number? ")

# Print message
print(favNumber)
```

This shows the message “What is your favorite number?” and stores whatever the user types into the favNumber variable. It will then print that number.

Now, let’s ask for the user’s favorite college:

```py
# Ask for favorite College
favCollege = input("What is your favorite college or university? ")

# Print message
print(“Your favorite college is”, favCollege)
```

Let's say the user inputs “Harvard”. 

Just like before, this will ask the question and store the answer (Harvard) in the variable favCollege. This time however, we give context to the message. The output will be “Your favorite college is Harvard”

We can of course combine our questions and print a final response containing both answers and their context.

```py
# Ask favorite number
favNumber = input("What is your favorite number? ")

# Ask for favorite College
favCollege = input("What is your favorite college or university? ")

# Print message
print("My favorite College is", favCollege, "and my favorite number is", favNumber)
```

This gives us a basic program that asks for information and prints it back to the user\!
