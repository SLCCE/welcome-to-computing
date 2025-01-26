It is a more complex task to accept user input in Java.

The object we'll use to accept user input is called a **Scanner**. A Scanner can be created using the following line of code:

```java
Scanner in = new Scanner(System.in);
```

Notice how we use the `new` keyboard to create a new **instance** of a Scanner. For most Objects, you will need to use this keyboard when defining a new copy of that Object. In the previous section, you saw that Strings were an exception to this rule, but it turns out the below two lines of code are identical:

```java
String s1 = "Test";
String s2 = new String("Test");
```

After you create your Scanner, you'll want to prompt your user on what you would like them to type in. Because the user will hit `Enter/Return` on their keyboard, we'll want to use `System.out.print()` when prompting the user, to avoid having too much blank space in the terminal.

```java
System.out.print("What is your favorite color? ");
```

The next line of code will depend on if we want to accept a String or a number. If we want to accept just the next word, we'll use the following line of code:

```java
String userInput = in.next();
```

If we want to accept the next integer, we'll use this line:

```java
int userInput = in.nextInt();
```

If we want to accept the next decimal number, we'll use this line:
```java
double userInput = in.nextDouble();
```

In this case, we are asking for the user's favorite color. The full code to get this user input is below.

```java
System.out.print("What is your favorite color? ");
String favColor = in.next();
```

Finally, we might want to output this to the user. We can use `System.out.println()` with **string addition** for this step.

```java
System.out.println("Your favorite color is " + favColor);
```

We only need one Scanner to collect all of the user input we need. We can continue to use the same Scanner. Once we have finished using the Scanner, it is a good practice to close it:

```java
in.close();
```

**EXERCISE:** make a copy of the `Java.java` starter code. Read each comment and fill in the missing code below.


