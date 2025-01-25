import java.util.Scanner;

public class Java {
  public static void main(String[] args) {
    // Create Scanner for input
    Scanner in = new Scanner(System.in);

    // Ask for favorite animal
    System.out.print("What is your favorite animal? ");
    String favAnimal = in.next();

    // Ask for favorite number
    System.out.print("What is your favorite number? ");
    int favNumber = in.nextInt();

    // Print message adding context to these variables
    System.out.println("My favorite animal is " + animal + "! My favorite number is " + favNumber + "!");
  }    
}
