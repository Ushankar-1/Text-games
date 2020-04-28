package com.company;

import java.util.Scanner;

public class Main {
/*
    public static void printBoard() {
        // THIS PRINTS THE BOARD. Either what the computer or the Player sees.
        System.out.print("  | A | B | C | D | E | F | G | H | I | J |\n-------------------------------------------\n");
        for (int r = 0; r < 10; r++) {
            if (r != 9) {
                System.out.print((r + 1) + " | ");
            } else {
                System.out.print((r + 1) + "| ");
            }
            for (int c = 0; c < 10; c++) {
                System.out.print(viewBoard[r][c] + " | "); // shipBoard is what computer sees, viewBoard is for the Player
            }
            System.out.print("\n-------------------------------------------\n");
        }
    }

    public static void copyBoard() {
        // This copies the shipBoard data to the viewBoard.
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                if (shipBoard[i][j] == 3) { //REMOVE THIS LATER
                    viewBoard[i][j] = "T";
                }
                if (shipBoard[i][j] == 0 || shipBoard[i][j] == 3) {
                    viewBoard[i][j] = " ";
                }
                if (shipBoard[i][j] == 1) {
                    viewBoard[i][j] = "O";
                }
                if (shipBoard[i][j] == 2) {
                    viewBoard[i][j] = "X";
                }
            }
        }
    }
*/
    public static void main(String[] args) {

        int[][] shipBoard = new int[10][10];
        // Value 0 = empty, 1 = miss, 2 = hit, 3 = ship

        String[][] viewBoard = new String[10][10];
        // This one's for the player to see



        // This copies the shipBoard data to the viewBoard.
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                if (shipBoard[i][j] == 0 || shipBoard[i][j] == 3) {
                    viewBoard[i][j] = " ";
                }
                if (shipBoard[i][j] == 1) {
                    viewBoard[i][j] = "O";
                }
                if (shipBoard[i][j] == 2) {
                    viewBoard[i][j] = "X";
                }
            }
        }






        // First ship: the 5-length one

        boolean ship5Sunk = false;

        // This block will be reused as well
        int randRow = (int) (Math.random() * 10);
        int randCol = (int) (Math.random() * 10);

        int zeroOrOne = (int) (Math.random() + 0.5);
        // 1 means vertical ship, 0 means horizontal

        // Safeguard to ensure valid ranges for the ship's location:
        while ((randRow - 2 < 0 || randRow + 2 >= 10) && (randCol - 2 < 0 || randCol + 2 >= 10)) {
            randRow = (int) (Math.random() * 10);
            randCol = (int) (Math.random() * 10);
        }


        // Giving the ship a location based on whether it is vertical or horizontal, and the random values:
        if (zeroOrOne == 1) {
            while (randRow - 2 < 0 || randRow + 2 >= 10) {
                randRow = (int) (Math.random() * 10);
            }
            for (int i = (randRow - 2); i <= randRow + 2; i++) {
                shipBoard[i][randCol] = 5;
            }
        } else {
            while (randCol - 2 < 0 || randCol + 2 >= 10) {
                randCol = (int) (Math.random() * 10);
            }
            for (int i = (randCol - 2); i <= randCol + 2; i++) {
                shipBoard[randRow][i] = 5;
            }
        }







        // Second ship: The four-length one

        boolean ship4Sunk = false;

        // This block will be reused as well
        randRow = (int) (Math.random() * 10);
        randCol = (int) (Math.random() * 10);

        zeroOrOne = (int) (Math.random() + 0.5);
        // 1 means vertical ship, 0 means horizontal

        int lOrR = (int) (Math.random() + 0.5);
        // 1 means 2 "ship" blocks are right/top of center, 0 means they're left/bottom of center, depending on zeroOrOne.

        // Giving the ship a location based on whether it is vertical or horizontal, and the random values:
        if (zeroOrOne == 0) { // If the ship is horizontal:
            if (lOrR == 0) { // And if it has 2 right of the "center" square:
                // (And make sure the values don't go out of bounds or intersect with other ships, IN THAT ORDER)
                while (randCol - 2 < 0 || randCol + 1 >= 10 || shipBoard[randRow][randCol-2] >= 3 || shipBoard[randRow][randCol-1] >= 3 || shipBoard[randRow][randCol] >= 3 || shipBoard[randRow][randCol+1] >= 3) {
                    randRow = (int) (Math.random() * 10);
                    randCol = (int) (Math.random() * 10);
                }
                for (int i = (randCol - 2); i <= randCol + 1; i++) {
                    shipBoard[randRow][i] = 4;
                }
            }
            if (lOrR == 1) { // And if it has 2 left of the "center" square
                // (And make sure the values don't go out of bounds or intersect with other ships, IN THAT ORDER)
                while (randCol - 1 < 0 || randCol + 2 >= 10 || shipBoard[randRow][randCol-1] >= 3 || shipBoard[randRow][randCol] >= 3 || shipBoard[randRow][randCol+1] >= 3 || shipBoard[randRow][randCol+2] >= 3) {
                    randRow = (int) (Math.random() * 10);
                    randCol = (int) (Math.random() * 10);
                }
                for (int i = (randCol - 1); i <= randCol + 2; i++) {
                    shipBoard[randRow][i] = 4;
                }
            }
        }
        if (zeroOrOne == 1) { // If the ship is vertical:
            if (lOrR == 0) { // And if it has 2 on top of the "center" square:
                // (And make sure the values don't go out of bounds or intersect with other ships, IN THAT ORDER)
                while (randRow - 2 < 0 || randRow + 1 >= 10 || shipBoard[randRow-2][randCol] >= 3 || shipBoard[randRow-1][randCol] >= 3 || shipBoard[randRow][randCol] >= 3 || shipBoard[randRow+1][randCol] >= 3) {
                    randRow = (int) (Math.random() * 10);
                    randCol = (int) (Math.random() * 10);
                }
                for (int i = (randRow - 2); i <= randRow + 1; i++) {
                    shipBoard[i][randCol] = 4;
                }
            }
            if (lOrR == 1) { //And if it has 2 below the "center" square:
                // (And make sure the values don't go out of bounds or intersect with other ships, IN THAT ORDER)
                while (randRow - 1 < 0 || randRow + 2 >= 10 || shipBoard[randRow-1][randCol] >= 3 || shipBoard[randRow][randCol] >= 3 || shipBoard[randRow+1][randCol] >= 3 || shipBoard[randRow+2][randCol] >= 3) {
                    randRow = (int) (Math.random() * 10);
                    randCol = (int) (Math.random() * 10);
                }
                for (int i = (randRow - 1); i <= randRow + 2; i++) {
                    shipBoard[i][randCol] = 4;
                }
            }
        }






        // Third and fourth ships: The three-length ones. For loop is so it runs twice separately to make the 2 ships. Surprisingly short.

        boolean ship31Sunk = false;
        boolean ship32Sunk = false;

        for (int i = 1; i <= 2; i++) {
            // This block will be reused as well
            randRow = (int) (Math.random() * 10);
            randCol = (int) (Math.random() * 10);

            zeroOrOne = (int) (Math.random() + 0.5);
            // 1 means vertical ship, 0 means horizontal

            // Giving the ship a location based on whether it is vertical or horizontal, and the random values:
            if (zeroOrOne == 1) {
                while (randRow - 1 < 0 || randRow + 1 >= 10 || shipBoard[randRow - 1][randCol] >= 3 || shipBoard[randRow][randCol] >= 3 || shipBoard[randRow + 1][randCol] >= 3) {
                    randRow = (int) (Math.random() * 10);
                    randCol = (int) (Math.random() * 10);
                }
                for (int j = (randRow - 1); j <= randRow + 1; j++) {
                    if (i == 1) {
                        shipBoard[j][randCol] = 31;
                    }
                    else {
                        shipBoard[j][randCol] = 32;
                    }
                }
            } else {
                while (randCol - 1 < 0 || randCol + 1 >= 10 || shipBoard[randRow][randCol - 1] >= 3 || shipBoard[randRow][randCol] >= 3 || shipBoard[randRow][randCol + 1] >= 3) {
                    randRow = (int) (Math.random() * 10);
                    randCol = (int) (Math.random() * 10);
                }
                for (int j = (randCol - 1); j <= randCol + 1; j++) {
                    if (i == 1) {
                        shipBoard[randRow][j] = 31;
                    }
                    else {
                        shipBoard[randRow][j] = 32;
                    }
                }
            }
        }





        // Final ship: The two-length one.

        boolean ship2Sunk = false;

        randRow = (int) (Math.random() * 10);
        randCol = (int) (Math.random() * 10);

        zeroOrOne = (int) (Math.random() + 0.5);
        // 1 means vertical ship, 0 means horizontal

        lOrR = (int) (Math.random() + 0.5);
        // 1 means 1 "ship" block is right/top of center, 0 means it's left/bottom of center, depending on zeroOrOne.

        // Giving the ship a location based on whether it is vertical or horizontal, and the random values:
        if (zeroOrOne == 0) { // If the ship is horizontal:
            if (lOrR == 0) { // And if it has 1 right of the "center" square:
                // (And make sure the values don't go out of bounds or intersect with other ships, IN THAT ORDER)
                while (randCol + 1 >= 10 || shipBoard[randRow][randCol] >= 3 || shipBoard[randRow][randCol+1] >= 3) {
                    randRow = (int) (Math.random() * 10);
                    randCol = (int) (Math.random() * 10);
                }
                for (int i = randCol; i <= randCol + 1; i++) {
                    shipBoard[randRow][i] = 20;
                }
            }
            if (lOrR == 1) { // And if it has 1 left of the "center" square
                // (And make sure the values don't go out of bounds or intersect with other ships, IN THAT ORDER)
                while (randCol - 1 < 0 || shipBoard[randRow][randCol-1] >= 3 || shipBoard[randRow][randCol] >= 3) {
                    randRow = (int) (Math.random() * 10);
                    randCol = (int) (Math.random() * 10);
                }
                for (int i = (randCol - 1); i <= randCol; i++) {
                    shipBoard[randRow][i] = 20;
                }
            }
        }
        if (zeroOrOne == 1) { // If the ship is vertical:
            if (lOrR == 0) { // And if it has 1 on top of the "center" square:
                // (And make sure the values don't go out of bounds or intersect with other ships, IN THAT ORDER)
                while (randRow + 1 >= 10 || shipBoard[randRow][randCol] >= 3 || shipBoard[randRow+1][randCol] >= 3) {
                    randRow = (int) (Math.random() * 10);
                    randCol = (int) (Math.random() * 10);
                }
                for (int i = randRow; i <= randRow + 1; i++) {
                    shipBoard[i][randCol] = 20;
                }
            }
            if (lOrR == 1) { //And if it has 1 below the "center" square:
                // (And make sure the values don't go out of bounds or intersect with other ships, IN THAT ORDER)
                while (randRow - 1 < 0 || shipBoard[randRow-1][randCol] >= 3 || shipBoard[randRow][randCol] >= 3) {
                    randRow = (int) (Math.random() * 10);
                    randCol = (int) (Math.random() * 10);
                }
                for (int i = (randRow - 1); i <= randRow; i++) {
                    shipBoard[i][randCol] = 20;
                }
            }
        }






        // The part where you actually play Battleship:

        Scanner scan = new Scanner(System.in);
        int row = 0;
        int col = 0;
        int shipCount = 5; // Number of "ship" squares existing
        int checkRow = 10; // Used to check if you repeated coordinates, start loop
        int checkCol; // Used to check if you repeated coordinates
        int turnsTaken = 0; // Counts turns
        int count5 = 0;
        int count4 = 0;
        int count31 = 0;
        int count32 = 0;
        int count2 = 0;

        //Prints the board once before start
        // THIS PRINTS THE BOARD. Either what the computer or the Player sees.
        System.out.print("  | A | B | C | D | E | F | G | H | I | J |\n-------------------------------------------\n");
        for (int r = 0; r < 10; r++) {
            if (r != 9) {
                System.out.print((r + 1) + " | ");
            } else {
                System.out.print((r + 1) + "| ");
            }
            for (int c = 0; c < 10; c++) {
                System.out.print(shipBoard[r][c] + " | "); // shipBoard is what computer sees, viewBoard is for the Player
            }
            System.out.print("\n-------------------------------------------\n");
        }

        //Loop part, loop just checks if any ships are still up
        while (shipCount != 0) {
            shipCount = 0;

            // This loop makes sure you don't repeat coordinates
            while (shipBoard[row][col] == 1 || shipBoard[row][col] == 2 || checkRow == 10) {

                // This block's for the column
                System.out.println("Which column? (A-J) ");
                String pCol = scan.nextLine();
                pCol = pCol.toUpperCase();
                while (pCol.equals("A") == false && pCol.equals("B") == false && pCol.equals("C") == false && pCol.equals("D") == false && pCol.equals("E") == false && pCol.equals("F") == false && pCol.equals("G") == false && pCol.equals("H") == false && pCol.equals("I") == false && pCol.equals("J") == false) {
                    System.out.println("Invalid. Please choose from the range A-J. ");
                    pCol = scan.nextLine();
                    pCol = pCol.toUpperCase();
                }

                if (pCol.equals("A")) {
                    col = 0; }
                if (pCol.equals("B")) {
                    col = 1; }
                if (pCol.equals("C")) {
                    col = 2; }
                if (pCol.equals("D")) {
                    col = 3; }
                if (pCol.equals("E")) {
                    col = 4; }
                if (pCol.equals("F")) {
                    col = 5; }
                if (pCol.equals("G")) {
                    col = 6; }
                if (pCol.equals("H")) {
                    col = 7; }
                if (pCol.equals("I")) {
                    col = 8; }
                if (pCol.equals("J")) {
                    col = 9; }


                // This block's for the row
                System.out.println("Which row? (1-10) ");
                String pRow = scan.nextLine();
                while (pRow.equals("1") == false && pRow.equals("2") == false && pRow.equals("3") == false && pRow.equals("4") == false && pRow.equals("5") == false && pRow.equals("6") == false && pRow.equals("7") == false && pRow.equals("8") == false && pRow.equals("9") == false && pRow.equals("10") == false) {
                    System.out.println("Invalid. Please choose from the range 1-10. ");
                    pRow = scan.nextLine();
                    pRow = pRow.toUpperCase();
                }
                if (pRow.equals("1")) {
                    row = 0;
                } else if (pRow.equals("2")) {
                    row = 1;
                } else if (pRow.equals("3")) {
                    row = 2;
                } else if (pRow.equals("4")) {
                    row = 3;
                } else if (pRow.equals("5")) {
                    row = 4;
                } else if (pRow.equals("6")) {
                    row = 5;
                } else if (pRow.equals("7")) {
                    row = 6;
                } else if (pRow.equals("8")) {
                    row = 7;
                } else if (pRow.equals("9")) {
                    row = 8;
                } else if (pRow.equals("10")) {
                    row = 9;
                }

                // This checks for repeating coordinates, prints message if so
                checkRow = row;
                checkCol = col;

                if (shipBoard[checkRow][checkCol] == 2 || shipBoard[checkRow][checkCol] == 1 ) {
                    System.out.println("You've already tried this square. Try a different one!");
                }
            }

            // Hit or miss messages and adjusting the shipBoard values to match
            if (shipBoard[row][col] >= 3) {
                shipBoard[row][col] = 2;
                System.out.println("\n\nI guess they never miss, huh? (Hit)\n");
            }

            if (shipBoard[row][col] == 0) {
                shipBoard[row][col] = 1;
                System.out.println("\n\nMiss.\n");
            }

            for (int i = 0; i < 10; i++) {
                for (int j = 0; j < 10; j++) {
                    if (shipBoard[i][j] == 5){
                        count5++;
                    }
                    if (shipBoard[i][j] == 4){
                        count4++;
                    }
                    if (shipBoard[i][j] == 31){
                        count31++;
                    }
                    if (shipBoard[i][j] == 32){
                        count32++;
                    }
                    if (shipBoard[i][j] == 20){
                        count2++;
                    }
                }
            }

            if (ship5Sunk == false && count5 == 0) {
                System.out.println("Ship sunk!\n");
                ship5Sunk = true;
            }
            if (ship4Sunk == false && count4 == 0) {
                System.out.println("Ship sunk!\n");
                ship4Sunk = true;
            }
            if (ship31Sunk == false && count31 == 0) {
                System.out.println("Ship sunk!\n");
                ship31Sunk = true;
            }
            if (ship32Sunk == false && count32 == 0) {
                System.out.println("Ship sunk!\n");
                ship32Sunk = true;
            }
            if (ship2Sunk == false && count2 == 0) {
                System.out.println("Ship sunk!\n");
                ship2Sunk = true;
            }

            count5 = 0;
            count4 = 0;
            count31 = 0;
            count32 = 0;
            count2 = 0;


            // Copies shipBoard's values to viewBoard
            for (int i = 0; i < 10; i++) {
                for (int j = 0; j < 10; j++) {
                    if (shipBoard[i][j] == 0 || shipBoard[i][j] >= 3) {
                        viewBoard[i][j] = " ";
                    }
                    else if (shipBoard[i][j] == 1) {
                        viewBoard[i][j] = "O";
                    }
                    else if (shipBoard[i][j] == 2) {
                        viewBoard[i][j] = "X";
                    }
                }
            }


            // THIS PRINTS THE BOARD. Either what the computer or the Player sees.
            System.out.print("  | A | B | C | D | E | F | G | H | I | J |\n-------------------------------------------\n");
            for (int r = 0; r < 10; r++) {
                if (r != 9) {
                    System.out.print((r + 1) + " | ");
                } else {
                    System.out.print((r + 1) + "| ");
                }
                for (int c = 0; c < 10; c++) {
                    System.out.print(shipBoard[r][c] + " | "); // shipBoard is what computer sees, viewBoard is for the Player
                }
                System.out.print("\n-------------------------------------------\n");
            }

            for (int i = 0; i < 10; i++) {
                for (int j = 0; j < 10; j++) {
                    if (shipBoard[i][j] >= 3) {
                        shipCount++;
                    }
                }
            }

            turnsTaken++;

        }

        System.out.println("YOU WIN! You sunk all 5 ships in "+turnsTaken+" turns!");
    }
}