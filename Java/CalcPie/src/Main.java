import java.util.Scanner;
import java.math.*;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        System.out.println("How many iterations?");
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.println("Starting "+ n +" iterations");
        double randomNumx;
        double randomNumy;
        long pie =0;

        for(int j =0; j < 100;j++) {
            for (int i = 0; i < n*100; i++) {
                randomNumx = (double) Math.random();
                randomNumy = (double) Math.random();

                if (randomNumx * randomNumx + randomNumy * randomNumy < 1) {
                    pie += 1;
                }
            }
            System.out.println(j+"%");
        }
        double calcpie = (4.0* pie) / (n*10000);
        String piStr = String.valueOf(calcpie);
        int maxLength = Math.min(n, piStr.length());

        System.out.println(piStr.substring(0, maxLength));
    }
}