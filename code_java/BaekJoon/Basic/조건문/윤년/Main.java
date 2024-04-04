package 조건문.윤년;

import java.io.*;
import java.util.StringTokenizer;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String input = br.readLine();
        StringTokenizer st = new StringTokenizer(input);

        int y = Integer.parseInt(st.nextToken());
        boolean answer ;
        if ((y%4==0 && y%100!=0) || y%400==0){
            answer = true;
        }
        else {
            answer = false;
        }
        if (answer){
            System.out.println(1);
        }
        else {
            System.out.println(0);
        }
        br.close();

    }
}
