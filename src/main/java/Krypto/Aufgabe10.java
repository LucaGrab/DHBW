
package Krypto;

import java.util.Arrays;

import static java.lang.Math.*;

public class Aufgabe10 {

    public static void main(String[] args) {
        int p = 191;
        int q = 167;
        int s = 599;
        int l = 100;
        double lDouble = l;
        if(valuesAreOK(p,q,s)){
            int[] bitArray = getBitfolge(p,q,s,l);
            for(int i = 1; i<bitArray.length;i++){
                System.out.print(bitArray[i]);
            }
            System.out.println();
            System.out.println("Anzahl an Runs: " + getRuns(getBitfolge(p,q,s,l)));
            System.out.println("Gewünschte Anzahl an Runs ist: " + (lDouble+1)/2);
        }

    }
    public static int[] getBitfolge(int p, int q, int s, int l){
        int[] xArray = new int[l+1];
        int[] bitArray = new int[l+1];
        int n = p*q;
        xArray[0] = (s*s)%n;
        for(int i = 1; i<=l; i++){
             xArray[i] = (xArray[i-1]*xArray[i-1])%n;
             bitArray[i] = xArray[i]%2;
        }
        return bitArray;
    }
    public static int getRuns(int[] bitArray){
        int runs = 0;
        for(int i = 0; i<bitArray.length-1;i++){
            if(bitArray[i+1]!=bitArray[i]) runs ++;
        }
        return runs;
    }

    public static boolean valuesAreOK(int p, int q, int s){
        if(p%4!=3||q%4!=3) return false;
        int n = p*q;
        if(ggt(n,s)!=1) return false;
        return true;
    }

    public static int ggt(int a, int b) {

        if (a == 0)
            return b;
        while (b != 0) {
            if (a > b)
                a = a - b;
            else
                b = b - a;
        }

        return a;
    }
}
