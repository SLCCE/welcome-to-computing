/*
 * todos: comments
 * exercise? -- could be separate object to make a toString for OR adding another attribute to the dice ex. color
 */
import java.util.Random;

public class Dice {
    private int sides;
    Random rand;
    
    Dice(int sides) {
        this.sides = sides;
        this.rand = new Random();
    }

    private int roll() {
        int val = this.rand.nextInt(sides) + 1;
        return val;
    }

    // @Override
    // public String toString() {
    //     return "Sides: " + sides;
    // }

    public static void main(String[] args) {
        // System.out.println("Hello World!");
        
        // roll the dice
        Dice d6 = new Dice(6);
        int rollValue = d6.roll();
        System.out.println(rollValue);

        // try to print out the dice object
        System.out.println(d6);
    }
}


