The syntax of Java is a bit different from Python. Consider the following Java code:

```java
public class Example {
  public static void main(String[] args) {
    System.out.println("Hello world!");
  }
}
```

As you can see, the program above will output "Hello world!" to the console. Notice, however, that there are a lot more lines of code. In upcoming workshops, we will cover the meaning of each term in more detail. For now, you can copy the code below and replace `// Code` with the code you would like to add and `Example` with the name of your file, excluding `.java`.

```java
public class Example {
  public static void main(String[] args) {
    // Code
  }
}
```

In short, all code in Java must be contained within a **class**. Here, the class is named *Example*. The code within the outer set of curly brackets is all contained within the *Example* class. Within each class are **methods**, or blocks of code which are run when they are **called**. When your program is run, Java will automatically call the *main()* method, running the code within the innser set of curly brackets.

Recall that the end of a line marked the end of a code **statement** in Java. As shown in the "Hello world!" example above, in Java, all **statements** must end in a semicolon (;). Thus, it is possible to end multiple 
