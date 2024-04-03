package 문자붙이기;
//10926
import java.io.*;
import java.util.StringTokenizer;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String input = br.readLine();
        StringTokenizer st = new StringTokenizer(input);
        String surprise = "??!";

        bw.write(st.nextToken()+surprise);
        bw.newLine();
        bw.flush();
        br.close();
        bw.close();
    }
}

