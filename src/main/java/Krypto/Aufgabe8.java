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
        for(int i = 1; i<150; i++){
            vigEnt(i);
        }
        //vigEnt(8);
        //getDopplungen();
    }

    public static void vigEnt(int sLänge){
        int[] schlüsselBeimWort = new int[bekanntesWort.length()];
        int[] chifIndex = new int[chifText.length()];
        chifIndex = getChifIndex();
        for(int i = 0; i<chifText.length()-bekanntesWort.length();i++){//Wort an jeder Stelle einsätzen - also der Anfang für den Schlüssel
            schlüsselBeimWort = getVerschiebung(i);
            String klarText = "";
            char[] klarTextArray = new char[chifText.length()];
            int schlüsselStartetBei = sLänge - i%sLänge;
            for(int j = 0; j<chifText.length();j++){
                if(schlüsselBeimWort.length>(j+schlüsselStartetBei) % sLänge) {
                    klarText += alphabet.charAt((chifIndex[j] - schlüsselBeimWort[(j+schlüsselStartetBei) % sLänge] + 27) % 27);
                }else{
                    klarText += chifText.toLowerCase().charAt(j);
                }
            }
            if(klarText.contains("VERSCHLUE")&&klarText.contains("UNVERSTAENDLICH")){
                System.out.println("KlarWort an Stelle "+i+" eingesetzt. Schlüssel Länge ist "+ sLänge + ". Klartext: "+ klarText);
            }
        }
    }

    public static int[] getVerschiebung(int stelle){
        int[] indexToReturn = new int[bekanntesWort.length()];
        for(int i = 0; i<bekanntesWort.length(); i++){
            for(int j = 0; j<alphabet.length();j++){
                if(chifText.toUpperCase().charAt(i+stelle)==alphabet.charAt(j)) {
                    indexToReturn[i] = j;
                }
            }
            for(int k = 0; k<alphabet.length();k++){
                if(bekanntesWort.toUpperCase().charAt(i)==alphabet.charAt(k)){
                    indexToReturn[i] = (indexToReturn[i] - k+27)%27;
                }
            }
        }
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

    public static void vigEntOldVersion(int sLänge){
        int[] schlüsselBeimWort =  new int[bekanntesWort.length()];
        int[] chifIndex = new int[chifText.length()];

        chifIndex = getChifIndex();
        for(int i = 0; i<chifText.length()-bekanntesWort.length();i++){//Wort an jeder Stelle einsätzen - also der Anfang für den Schlüssel
            schlüsselBeimWort = getVerschiebung(i);
            String klarText = "";
            char[] klarTextArray = new char[chifText.length()];
            boolean wiederAmAnfang = false;
            for(int j = 0; j<chifText.length();j++){
                int currentPosition = (j+i)%chifText.length();
                if(currentPosition==0) wiederAmAnfang = true;
                if((schlüsselBeimWort.length>j%sLänge)&&!wiederAmAnfang) {
                    klarTextArray[currentPosition] = alphabet.charAt((chifIndex[currentPosition] - schlüsselBeimWort[j % sLänge] + 27) % 27);
                    klarText += alphabet.charAt((chifIndex[currentPosition] - schlüsselBeimWort[j % sLänge] + 27) % 27);

                }else if((schlüsselBeimWort.length>j%sLänge)&&wiederAmAnfang){
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


}
