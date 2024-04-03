package 꼬마정민;
//11382
import java.io.*;
import java.util.StringTokenizer;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String input = br.readLine();
        StringTokenizer st = new StringTokenizer(input);

        long A = Long.parseLong(st.nextToken());
        long B = Long.parseLong(st.nextToken());
        long C = Long.parseLong(st.nextToken());

        String result = Long.toString(A+B+C);

//        int spot_index = result.indexOf(".");
//        String answer = result.substring(0,spot_index);
        bw.write(result);
        bw.flush();
        br.close();
        bw.close();
    }
}