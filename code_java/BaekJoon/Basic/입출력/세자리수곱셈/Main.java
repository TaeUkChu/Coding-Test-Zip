package 세자리수곱셈;

import java.io.*;
// import java.util.StringTokenizer;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

//        StringTokenizer st = new StringTokenizer(br.readLine());

        int number_one = Integer.parseInt(br.readLine());
        int number_two = Integer.parseInt(br.readLine());

        bw.write(Integer.toString(number_one * (number_two % 10)));
        bw.newLine();
        bw.write(Integer.toString(number_one * ((number_two % 100 / 10))));
        bw.newLine();
        bw.write(Integer.toString(number_one * (number_two / 100)));
        bw.newLine();
        bw.write(Integer.toString(number_one * number_two));
        bw.flush();
        br.close();
        bw.close();
    }
}