package Krypto;

public class Aufgabe1 {
    static String alphabet = "abcdefghijklmnopqrstuvwxyz";

    public static void main(String[] args) {
        String chifText = "fgnexrirefpuyhrff";
        getCaesar(getIndexArray(chifText));
    }

    public static int getIndex(Character chara) {
        for (int i = 0; i < alphabet.length(); i++) {
            if (chara == alphabet.charAt(i)) {

                return i;
            }
        }
        return -1;
    }

    public static int[] getIndexArray(String chifText) {
        int[] chifIndexArray = new int[chifText.length()];
        for (int i = 0; i < chifIndexArray.length; i++) {
            chifIndexArray[i] = getIndex(chifText.charAt(i));
        }
        return chifIndexArray;
    }
    public static void getCaesar(int[] indexArray){
        String[] caesarStringArray = new String[alphabet.length()];
        for(int a = 0; a < alphabet.length(); a++){
            caesarStringArray[a] = "";
        }
        for( int i = 0; i < alphabet.length(); i++){
            for( int j = 0; j < indexArray.length; j++){

                caesarStringArray[i] = caesarStringArray[i] + alphabet.charAt((i+indexArray[j])%26);
            }
       }
        for( int z = 0; z<caesarStringArray.length; z++){
            System.out.println(caesarStringArray[z]);
        }
        //sout
    }

}
