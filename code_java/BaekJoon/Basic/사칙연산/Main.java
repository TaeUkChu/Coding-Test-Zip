package 사칙연산;

import java.io.*;
import java.util.StringTokenizer;

// 10869
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(Integer.toString(A+B)); // 출력 시엔 String형으로 변환해 출력해야 함.
        bw.newLine();
        bw.write(Integer.toString(A-B));
        bw.newLine();
        bw.write(Integer.toString(A*B));
        bw.newLine();
        bw.write(Integer.toString(A/B));
        bw.newLine();
        bw.write(Integer.toString(A%B));
        br.close();
        bw.close();
    }
}
