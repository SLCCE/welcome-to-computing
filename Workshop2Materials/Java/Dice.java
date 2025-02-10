import java.util.Random;

/**
 * A class for making a rolling dice
 */
public class Dice {
    /** store the number of sides */
    private int sides;
    /** Random object to simulate rolling */
    Random rand;
    
    /**
     * Constructs a dice object
     */
    Dice(int sides) {
        this.sides = sides;
        this.rand = new Random();
    }

    /**
     * returns a random value from 1 to sides
     */
    private int roll() {
        // nextInt(sides) generates a number from 0 to sides - 1, adjust it by +1
        int val = this.rand.nextInt(sides) + 1;
        return val;
    }

    // Uncomment this after running the program once to see the result!
    // @Override
    // public String toString() {
        // return "Sides: " + sides;
    // }

    public static void main(String[] args) {
        // System.out.println("Hello World!");
        
        // roll the dice
        Dice d6 = new Dice(6);
        int rollValue = d6.roll();
        System.out.println(rollValue);

        // try to print out the dice object
        System.out.println(d6);

        // exercise: add an attribute (ex. color) and modify the toString function to print out the information
    }
}


