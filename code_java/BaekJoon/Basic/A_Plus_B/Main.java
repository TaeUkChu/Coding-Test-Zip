package A_Plus_B;

import java.io.*;
import java.util.Scanner;
import java.util.StringTokenizer;


public class Main {
    public static void main(String[] args) throws IOException {
        /*
        // 입력 받는 방식 1
        Scanner input = new Scanner(System.in);
        int A = input.nextInt();
        int B = input.nextInt();
        */

        // 입력 받는 방식 2
        System.out.println("버퍼 Reader 시작");
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));


        StringTokenizer st = new StringTokenizer(br.readLine());

        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());
        double result = (double)A/(double)B;

//        int result = A+B;

        /*
        // 출력 하는 방식 1
        out.println("A = " + A + ",B = " + B);
        out.println("A+B = " + result);
        */

        // 출력하는 방식 2
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(Double.toString(result));
        br.close();
        bw.close();
        System.out.println("버퍼 Reader 종료");

    }
}
