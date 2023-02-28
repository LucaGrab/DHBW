package Krypto;

import java.util.HashMap;
import java.util.Map;

public class Aufgabe3 {

    static String alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    public static void main(String[] args) {
        String klarText = "Es ist der Vater mit seinem Kind;\n" +
                "Er hat den Knaben wohl in dem Arm,\n" +
                "Er fasst ihn sicher, er hält ihn warm.\n" +
                "\n" +
                "\"Mein Sohn, was birgst du so bang dein Gesicht?\"\n" +
                "\"Siehst, Vater, du den Erlkönig nicht?\n" +
                "Den Erlkönig mit Kron und Schweif?\"\n" +
                "\"Mein Sohn, es ist ein Nebelstreif.\"\n" +
                "\n" +
                "\"Du liebes Kind, komm, geh mit mir!\n" +
                "Gar schöne Spiele spiel ich mit dir;\n" +
                "Manch bunte Blumen sind an dem Strand;\n" +
                "Meine Mutter hat manch gülden Gewand.\"\n" +
                "\n" +
                "\"Mein Vater, mein Vater, und hörest du nicht,\n" +
                "Was Erlenkönig mir leise verspricht?\"\n" +
                "\"Sei ruhig, bleibe ruhig, mein Kind;\n" +
                "In dürren Blättern säuselt der Wind.\"\n";
        System.out.println(countChars(klarText.toUpperCase()));
        System.out.println(calcIndex(countChars(klarText.toUpperCase())));

    }

    public static Map countChars  (String klarText){
        Map<Character,Integer> charMap = new HashMap<Character,Integer>();

        for(int j = 0; j<alphabet.length();j++){
            charMap.put(alphabet.charAt(j),0);
        }


        for(int i = 0; i< klarText.length();i++){
            if(charMap.get(klarText.charAt(i))  != null){
                charMap.put(klarText.charAt(i), charMap.get(klarText.charAt(i))+1);
            }
        }
        return charMap;
    }

    public static double calcIndex (Map<Character,Integer> charMap){
        int length = 0;
        for (Map.Entry<Character, Integer> entry :
                charMap.entrySet()) {
            length += entry.getValue();
        }
        System.out.println(length);
        double index = 0.0;
        for (Map.Entry<Character, Integer> entry :
                charMap.entrySet()) {
            double converted = entry.getValue();
            index += Math.pow(converted/length,2);
        }
        return index;
    }
}
