package com.company;
import java.util.Scanner;
import java.lang.Character;

import static java.lang.Character.*;
import static java.lang.String.copyValueOf;


public class Main {

    public static void main(String[] args) {

        System.out.println("\n\nThis works as both an encrypter and decrypter! Input the desired phrase to receive\n" +
                "both the encrypter/decrypted version and the key: ");
        Scanner scan = new Scanner(System.in);
        String tempStr = scan.nextLine(); //Input
        int length = tempStr.length(); //Length of string, also 1 greater than length of str, the char[]
        char[] str = tempStr.toCharArray(); //Turns the input string into a char[]

        char[] strOriginal = new char[length];
        for(int i = 0; i < length; i++) { // Saves the original str as a "baseline" to modify, and save the mods to str
            strOriginal[i] = str[i];
        }



        //Normal lowercase English letters: Unicode 97-122, inclusive. Uppercase: 65-90, inclusive.
        // Unicode basic Latin chart: (0-127): https://www.ssec.wisc.edu/~tomw/java/unicode.html#x0000

        System.out.println("\nThe original text: "+tempStr+"\n");

        for(int shift = 1; shift < 26; shift++) { //Key of +shift for caesar cipher

            for(int i = 0; i < length; i++){ //Runs through all of char[]

                int uni = codePointAt(strOriginal, i); //the unicode of a character from the original string
                if(isLetter(strOriginal[i])) { //So it only modifies letters, not symbols

                    if(uni+shift > 122) { // In case it's a lowercase letter going to overshoot
                        int adjust = 122-uni; // distance shift covers before overshoot
                        uni = 96+shift-adjust; // The unicode for "a" plus the distance not covered by shift before overshoot.
                    }
                    else if(uni+shift > 90 && uni < 91) { // In case it's an uppercase letter going to overshoot
                        int adjust = 90-uni; // distance shift covers before overshoot
                        uni = 64+shift-adjust; // The unicode for "A" plus the distance not covered by shift before overshoot.
                    }
                    else { // If it can work normally, no overshoot
                        uni += shift;
                    }

                    str[i] = (char)uni; // Modifying the str
                }
            }
            String newStr = copyValueOf(str, 0, length);
            int reverse = 26 - shift; // This variable shows which key is for decrypting.

            // This if/else statement just makes sure the encrypted strings line up pearlfectly.
            if(shift < 10){
                System.out.println("Key of  +"+shift+": "+newStr+"\t(Key of +"+reverse+" if decrypting.)");
            }
            else {
                System.out.println("Key of +"+shift+": "+newStr+"\t(Key of +"+reverse+" if decrypting.)");
            }
        }
    }
}
