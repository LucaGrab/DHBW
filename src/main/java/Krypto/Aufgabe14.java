package Krypto;

import java.util.Arrays;

public class Aufgabe14 {
    public static void main(String[] args) {
        Sieb(10000, 1000);
    }
    public static void Sieb(int maxNumber, int primZahlAnStelle){
        boolean[] isPrimArray = new boolean[maxNumber+1];
        for(int i = 0; i<maxNumber+1; i++){ //alle auf true setzen außer 2er Reihe (erster Druchgang direkt dabei)
            if(i%2==0){
                isPrimArray[i] = false;
            }else{
                isPrimArray[i] = true;
            }
        }
        int counter = 0;
        for(int i = 2; i<maxNumber; i++){//das ist die Primzahl
            if(isPrimArray[i]){//Ist eine Primzahl
                counter++;
                System.out.println(i);
                if(counter==primZahlAnStelle){
                    System.out.println("Die " + counter + "te Primzahl ist " + i);
                }
                for(int j = i+1; j<maxNumber+1;j++){//wird durchgesiebt
                    if(j%i==0){
                        isPrimArray[j] = false;//ist keine Primzahl
                    }
                }
            }

        }
        /*for(int i = 1; i<maxNumber+1;i++){
            if(isPrimArray[i]){
                System.out.println(i);
            }
        }
        System.out.println(Arrays.toString(isPrimArray));*/
    }
}
