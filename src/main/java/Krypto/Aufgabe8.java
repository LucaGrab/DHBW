package Krypto;

public class Aufgabe8 {
    /*static String chifText = "wtlfpqktzbgdxwjswcrfxwjr\n" +
            "lcyladajwhraeszqvlqakhaw\n" +
            "sspfccozepyoqfrh.nfupxxl\n" +
            "wbquqhxuctaipbdqdlaiuqjk\n" +
            "dkgighxq.yfbawjplktfgeoh\n" +
            "yplaxhsijdywuubtzwsfhvob\n" +
            "lyeaeszqwtlfpyohjnfmjhbi\n" +
            "wwrfpqktzbgdxwjswcrfxwjr\n" +
            "lcyeupjtztdgghcvodyqes\n";*/
    static String chifText = "wtlfpqktzbgdxwjswcrfxwjrlcyladajwhraeszqvlqakhawsspfccozepyoqfrh.nfupxxlwbquqhxuctaipbdqdlaiuqjkdkgighxq.yfbawjplktfgeohyplaxhsijdywuubtzwsfhvoblyeaeszqwtlfpyohjnfmjhbiwwrfpqktzbgdxwjswcrfxwjrlcyeupjtztdgghcvodyqes";
    static String alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ.";
    //static String bekanntesWort = "KRYPTOGRAFIE";
    static String bekanntesWort = "VERSCHLUESSELUNG";

    public static void main(String[] args) {
        //System.out.println(Arrays.toString(getVerschiebung(0)));
        //System.out.println(Arrays.toString(getChifIndex()));
        /*for(int i = 1; i<20; i++){
            ent(i);
        }*/
        ent(8);
        //getDopplungen();
        //System.out.println(chifText.indexOf("rfxwjr"));
        //System.out.println(chifText.indexOf("rfxwjr",20));
    }
    public static void getDopplungen(){
        for(int i = 0; i<chifText.length()-5;i++){
            String substring = chifText.substring(i,i+3);
            int subStringCounter = 0;
            if(chifText.indexOf(substring,i+1)!=-1){
                System.out.println("subString: " + substring);
                //System.out.println("anzahl: " + subStringCounter);
                System.out.println("index: "+ chifText.indexOf(substring,i+1));
                System.out.println("sLänge: " + (chifText.indexOf(substring,i+1)- i));
            }

        }
    }

    public static void ent(int sLänge){
        int[] schlüsselBeimWort = new int[bekanntesWort.length()];
        int[] chifIndex = new int[chifText.length()];

        chifIndex = getChifIndex();
        for(int i = 0; i<chifText.length()-bekanntesWort.length();i++){//Wort an jeder Stelle einsätzen - also der Anfang für den Schlüssel
            schlüsselBeimWort = getVerschiebung(i);
            //if(i<2) System.out.println(Arrays.toString(schlüsselBeimWort));
            String klarText = "";
            char[] klarTextArray = new char[chifText.length()];
            boolean wiederAmAnfang = false;
            for(int j = 0; j<chifText.length();j++){
                int currentPosition = (j+i)%chifText.length();
                if(currentPosition==0) wiederAmAnfang = true;
                if((schlüsselBeimWort.length>j%sLänge)&&!wiederAmAnfang) {
                    if (i == 131 && (currentPosition > 205 || currentPosition < 5)) {
                        //System.out.println(j%sLänge);
                        /*System.out.println("j%sLänge: " + j % sLänge);
                        System.out.println("position: " + currentPosition);
                        System.out.println("chifIndex: " + chifIndex[currentPosition]);
                        System.out.println("chifBuchstabe: " + alphabet.charAt(chifIndex[currentPosition]));
                        System.out.println("schlüssel: " + (schlüsselBeimWort[j % sLänge]));
                        System.out.println("buchstaben index:" + (chifIndex[currentPosition] - schlüsselBeimWort[j % sLänge] + 27) % 27);
                        System.out.println("richtiger buchstabe: " + alphabet.charAt((chifIndex[currentPosition] - schlüsselBeimWort[j % sLänge] + 27) % 27));*/
                    }
                    klarTextArray[currentPosition] = alphabet.charAt((chifIndex[currentPosition] - schlüsselBeimWort[j % sLänge] + 27) % 27);
                    klarText += alphabet.charAt((chifIndex[currentPosition] - schlüsselBeimWort[j % sLänge] + 27) % 27);


                }else if((schlüsselBeimWort.length>j%sLänge)&&wiederAmAnfang){
                    if (i == 131 && (currentPosition > 205 || currentPosition < 15)) {
                        //System.out.println(currentPosition%sLänge);
                    }
                    klarTextArray[currentPosition] = alphabet.charAt((chifIndex[currentPosition] - schlüsselBeimWort[(currentPosition+5) % sLänge] + 27) % 27);
                    klarText += alphabet.charAt((chifIndex[currentPosition] - schlüsselBeimWort[(currentPosition+5) % sLänge] + 27) % 27);


                }else if(schlüsselBeimWort.length<=j%sLänge){
                    klarTextArray[currentPosition] = chifText.toLowerCase().charAt(currentPosition);
                    klarText += chifText.toLowerCase().charAt(currentPosition);
                }
            }

            if(klarText.contains("VERSCHLUE")&&klarText.contains("EINE")){
                    System.out.println("KlarWort an Stelle: "+i+"sLänge: "+ sLänge + "text: "+ klarText);
                    for(int c = 0; c<klarTextArray.length; c++){
                        System.out.print(klarTextArray[c]);
                    }
            }
        }
    }

    public static int[] getVerschiebung(int stelle){
        int[] indexToReturn = new int[bekanntesWort.length()];
        for(int i = 0; i<bekanntesWort.length(); i++){
            for(int j = 0; j<alphabet.length();j++){
                if(chifText.toUpperCase().charAt(i+stelle)==alphabet.charAt(j)) {
                    indexToReturn[i] = j;
                    /*if(i==0){
                        System.out.println("i+stelle: "+ (i+stelle));
                        System.out.println("im chif text: "+ chifText.toUpperCase().charAt(i+stelle));
                        System.out.println("an stelle 9 hier: " + j);
                    }*/
                }
            }
            for(int k = 0; k<alphabet.length();k++){
                if(bekanntesWort.toUpperCase().charAt(i)==alphabet.charAt(k)){
                    indexToReturn[i] = (indexToReturn[i] - k+27)%27;
                    /*if(i==0){
                        System.out.println("k: "+ (k));
                        System.out.println("im wort: "+ bekanntesWort.toUpperCase().charAt(i));
                        System.out.println("schlüssel: " + indexToReturn[i]);
                    }*/
                }
            }
        }
        boolean firstDoppelt = false;
        boolean secondDoppelt = false;
        boolean thridDoppelt = false;


        /*for(int b = 3; b<indexToReturn.length;b++){
            if(indexToReturn[0]==indexToReturn[b]){
                firstDoppelt = true;
            }
            if(indexToReturn[1]==indexToReturn[b]){
                secondDoppelt = true;
            }
            if(indexToReturn[2]==indexToReturn[b]){
                thridDoppelt = true;
            }
        }
        if(firstDoppelt&&secondDoppelt&&thridDoppelt)System.out.println(Arrays.toString(indexToReturn));*/

        //System.out.println(Arrays.toString(indexToReturn));
        return indexToReturn;
    }

    public static int[] getChifIndex(){
        int[] indexToReturn = new int[chifText.length()];
        for(int i = 0; i<chifText.length(); i++){
            for(int j = 0; j<alphabet.length(); j++){
                if(chifText.toUpperCase().charAt(i)==alphabet.charAt(j)){
                    indexToReturn[i] = j;
                }
            }
        }
        return indexToReturn;
    }


}
