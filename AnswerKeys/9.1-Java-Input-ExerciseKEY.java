import java.util.Scanner;

public class JavaInputExerciseKEY {
    public static void main(String args[]) {
        // 1. make a scanner to begin receiving input through System.in (standard input)
        Scanner scan = new Scanner(System.in);
        // 2. print a question asking the user for their favorite letter
        System.out.println("What is your favorite letter?");
        // 3. store the user's favorite letter in a variable
        String favoriteLetter = scan.next();
        // 4. print "Your favorite letter is" followed by their favorite letter
        System.out.println("Your favorite letter is " + favoriteLetter);


        // 5. print a question asking the user for a number
        System.out.println("Enter a number");
        // 6. store the number into a variable -- use scan.nextInt()
        int x1 = scan.nextInt();
        // 7. ask the user for anotoher number
        System.out.println("Enter another number");
        // 8. store the second number into a separate variable
        int x2 = scan.nextInt();
        // 9. print "The sum of your numbers is" followed by the sum of the two numbers
        System.out.println("The sum of your numbers is " + (x1 + x2));
        // 10. close the scanner
        scan.close();
    }
}
