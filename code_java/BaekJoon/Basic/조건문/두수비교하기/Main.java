package 조건문.두수비교하기;

import java.io.*;
import java.util.StringTokenizer;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String input = br.readLine();
        StringTokenizer st = new StringTokenizer(input);

        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());

        String answer;

        if (A > B) {
            answer = ">";
        } else if (A < B) {
            answer = "<";
        }
        else {
            answer = "==";
        }
        bw.write(answer);

        bw.flush();
        br.close();
        bw.close();
    }
}
