package com.company;
import java.lang.Math;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

	String[] firstHalf = new String[]{"Water", "Fire", "Wind", "Sky", "Earth", "Sea", "Storm", "Blood", "Night", "Frost", "Dust", "Star", "Heart", "Soul", "Light", "Dark", "Shadow", "Sun", "Moon", "Glass", "Steel", "Iron", "Stone", "Silence", "Song", "Void", "Color", "Flame", "Winter", "World"};
	String[] lastHalf = new String[]{"cast", "blown", "sung", "spun", "bound", "born", "lost", "wrought", "forged", "margin", "torn", "heart", "souled", "fell", "rise", "set", "touched", "shadowed", "fired", "winged", "blood", "weight", "locked", "tale", "maw"};

	// System.out.println(firstHalf.length+" "+lastHalf.length+"\n");

    String input = "1";

	while(input.equals("1")) {
	    for (int i = 1; i < 6; i++) {

            int firstNum = (int) (Math.random() * (firstHalf.length));
            int lastNum = (int) (Math.random() * lastHalf.length);
            String title = (firstHalf[firstNum]) + (lastHalf[lastNum]);
            System.out.println(i+". "+title);
        }

        Scanner scan = new Scanner(System.in);
        System.out.println("\nEnter \"1\" to continue, or anything else to exit.\n ");
        input = scan.nextLine();
    }







    }
}
