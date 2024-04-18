package 조건문.주사위세개;

import java.io.*;
import java.util.StringTokenizer;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String input = br.readLine();
        StringTokenizer st = new StringTokenizer(input);

        int one = Integer.parseInt(st.nextToken());
        int two = Integer.parseInt(st.nextToken());
        int three = Integer.parseInt(st.nextToken());
        int answer = 0;

        //노가다 방법 1

        if (one == two && two == three) {
            answer = 10000 + one*1000;
        }
        else if (one == two && one != three){
            answer = 1000 + one*100;
        }else if (one == three && one != two){
            answer = 1000 + one*100;
        }else if (three == two && one != three){
            answer = 1000 + three*100;
        } else if (one > two && one > three) {
            answer = 100*one;
        }else if (two > one && two > three) {
            answer = 100*two;
        }else if (three > two && three > one) {
            answer = 100*three;
        }
        bw.write(Integer.toString(answer));
        bw.flush();
        br.close();
        bw.close();
    }
}