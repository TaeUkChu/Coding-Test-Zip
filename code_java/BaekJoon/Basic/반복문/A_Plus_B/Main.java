package 반복문.A_Plus_B;

import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int N = input.nextInt();
        String test;
        StringTokenizer st;

        for (int i=0; i<N; i++){
            test = input.nextLine();
            st = new StringTokenizer(test);

            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());

            System.out.println(A+B);
        }
    }

}
