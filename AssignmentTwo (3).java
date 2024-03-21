W2w/*
Computer Science 30 Assignment Two
Assorted things to solve.  Now with loops!
Name: Sharon
Date: 10/16/2023
 */

import java.util.Scanner;

public class AssignmentTwo {

    /*
    Use a for loop to print the even number from 2 to 100, inclusive.
     */
    public static void even() {
        // for loop for counting 2 to 100
        for (int count = 2; count <= 100; count += 2) {
            System.out.println(count);
        }

    }

    /*
    Ask the user how many integers they want to sum.  Use a while loop to ask for and sum that many numbers.  Keep track
    of the count of how many negative entries, positive entries, and entries equal to 0 that there were.  Use an
    if\else if\ else chain instead of separate if statements to do this.  Display the sum and the other stats at the
    end.

    Possible program run:

    How many integers do you want to sum?  3

    Enter integer: -1
    Enter integer: 0
    Enter integer: -10

    Sum: -11
    Number of zeroes: 1
    Number of negative integers: 2
    Number of positive integers: 0
     */
    public static void sumStats() {
        Scanner inputs = new Scanner(System.in);
        System.out.print("How many integers do you want to sum ? ");
        int user = inputs.nextInt();
        // variable to count number
        int number1 = 0;
        int number2 = 0;
        int number3 = 0;
        int total = 0;


        while (0 < user) {
            user--;
            Scanner answer = new Scanner(System.in);
            System.out.print("Enter integer: ");
            int number = answer.nextInt();

            // if-else, if statements

            if (number > 0) {
                number1 += 1;
            } else if (number < 0) {
                number2 += 1;

            } else {
                number3 += 1;

            }
            total += number;
        }
        System.out.println("number of postive :" + number1);
        System.out.println("number of negative :" + number2);
        System.out.println("number of zero :" + number3);
        System.out.println("Sum is equal to: " + total);
    }

    /*
    Asks the user how many coin flips they wish to simulate.  Use a loop to simulate flipping a coin that many times.
    Output the total number flips, number of heads, percentages of heads, number of tails, and  percentage of tails.
     */
    public static void coinFlipper() {

        Scanner inputs = new Scanner(System.in);
        System.out.print("How many times would you like to flip the coin ? ");
        int coin = inputs.nextInt();
        int heads = 0;
        int tails = 0;
        double num = coin;


        while (0 < coin) {
            coin--;
            System.out.println("Flipping Coin...");
            int rnd = (int) (Math.random() * 6);
            if (rnd <= 3) {
                heads += 1;
            } else if (rnd > 3) {
                tails += 1;
            }

        }

        //  to calculate the percentages and print out values

        double headP = heads / num * 100;
        System.out.print("number of heads : " + heads);
        System.out.println(" ----> " + headP + "%");

        double tailP = tails / num * 100;
        System.out.print("number of tails : " + tails);
        System.out.println(" ----> " + tailP + "%");
    }

    public static void main(String[] args) {
        even();
        System.out.println();

        sumStats();
        System.out.println();

        coinFlipper();
    }
}
