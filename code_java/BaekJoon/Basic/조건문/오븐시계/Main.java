package 조건문.오븐시계;

import java.io.*;
import java.util.StringTokenizer;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String input = br.readLine();
        StringTokenizer st = new StringTokenizer(input);

        int hour = Integer.parseInt(st.nextToken());
        int min = Integer.parseInt(st.nextToken());
        int dial = Integer.parseInt(br.readLine());

        min += dial;

        while (min > 60){
            min -= 60;
            hour += 1;
        }
        if (hour > 24)




        bw.write(st.nextToken());
        bw.newLine();
        bw.flush();
        br.close();
        bw.close();
    }
}
