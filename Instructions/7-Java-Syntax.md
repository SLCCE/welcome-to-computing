# Java Syntax

The syntax of Java is a bit different from Python. Consider the following Java code:

```java
public class Example {
  public static void main(String[] args) {
    System.out.println("Hello world!");
  }
}
```

As you can see, the program above will output "Hello world!" to the console. Notice, however, that there are a lot more lines of code. In upcoming workshops, we will go into detail on the meaning of each component. For now, you can copy the code below and replace `// Code` with the code you would like to add and `Example` with the name of your file, excluding `.java`.

```java
public class Example {
  public static void main(String[] args) {
    // Code
  }
}
```

In short, all code in Java must be contained within a **class**. Here, the class is named *Example*. The code within the outer set of curly brackets is all contained within the *Example* class. Within each class are **methods**, or blocks of code which are run when they are **called**. When your program is run, Java will automatically call the *main()* method, running the code within the innser set of curly brackets.

Recall that the end of a line marked the end of a code **statement** in Java. As shown in the "Hello world!" example above, in Java, all **statements** must end in a semicolon (;). Thus, it is possible to write multiple statements of code on the same line, so long as each statement ends with a semicolon. In practice, however, programmers like to keep their code readable, so they will keep to one statement per line.

Here's what a function looks like:
```java
public int addTwoNumbers(int x, int y) {
  return x + y;
}
// prints out 5
System.out.println(addTwoNumbers(2, 3));
```
From the function header, we can see that it has public visibility, returns an integer, is called 'addTwoNumbers,' and takes two integer parameters, x and y. As for the function body, it returns the sum of the two numbers. 

Java has static typing, so the type of the variable needs to be declared. 
```java
int x = 1
double y = 2.3
```

In Java, you can use `//` to denote a comment. In addition to single-line comments, Java also includes multi-line comments, as shown in the examples below. Java will ignore all text contained within a comment, so you do not need to end each line of comments with a semicolon.

```java
// This is a
// group of
// single-line
// comments.
// Notice how
// each line
// must start
// with two
// slashes.
```

```java
/*
  This is a
  multiline
  comment.
  Notice
  the symbols
  we use to
  mark the
  beginning
  and end of
  these comments.
*/
```
