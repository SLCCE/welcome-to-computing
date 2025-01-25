Like Python, Java can also use **variables** to store data. Unlike Python, which is a dynamically-typed language, Java is statically-typed, meaning that you must tell Java what kind of variable you are using.

**Primitive** types are simpler, representing types predefined by Java. Primitives start with a lowercase letter. The code below shows examples of several different primitive types that we will be using throughout our workshops:

```java
public class PrimitiveTypes {
  public static void main(String[] args) {
    int number = 3;
    double decimal = 4.6;
    character ch = 'E';
    boolean b = true;
  }
}
```

**Objects** are more complex. Objects start with a capital letter. They are the result of combining primitive types and other Objects together. The first Object type we will discuss is a String. What type(s) do you think are added together to make a String?

```java
public class ObjectType {
  public static void main(String[] args) {
    String s = "Hello, world!";
  }
}
```


Java provides several options to print out a line of text. We'll focus on two of them.

```java
System.out.print("Text"); // Option 1
System.out.println("Text"); // Option 2
```

These print statements are very similar, with the only difference being that `System.out.print()` will print out only the text you provide; while `System.out.println()` adds a new line at the end of your message, similar to hitting *Enter/Return* on your keyboard. `System.out.println()` works similarly to Python's `print()` function. Often, your last print statement will need to be a `System.out.println()` statement in order for all of your text to display properly in your terminal.

To see this visually, try running the two blocks of code below.

```java
System.out.print("One");
System.out.println("Two");
```

```java
System.out.println("One");
System.out.println("Two");
```


