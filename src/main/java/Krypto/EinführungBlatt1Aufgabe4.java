package Krypto;

public class EinführungBlatt1Aufgabe4 {
    public static void main(String[] args) {
        //collatz(3,1,27);
        for(int i = 1; i<21;i++){
            collatz(3,7,i);
        }
    }
    public static void collatz(int a, int b, int n){
        int startValue = n;
        int counterSteps = 0;
        boolean nope = false;
        while(n!=1){
            if(n%2==0){
                n = n/2;
            }else{
                n = n*a+b;
            }
            counterSteps++;
            if(counterSteps==1000){
                nope = true;
                break;
            }
        }
        if(!nope){
            //System.out.println(startValue + " hat soviele Schritte: " + counterSteps);
        }else{
            System.out.println(startValue + " ist nach 1000 Schritten noch nicht durch");
        }
    }
}
