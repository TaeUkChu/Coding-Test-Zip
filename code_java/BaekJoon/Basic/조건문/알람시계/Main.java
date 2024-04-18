package 조건문.알람시계;
//2884
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

        if (min - 45 < 0) {
            hour -= 1;
            min += 15;
        }
        else {
            min-=45;
        }

        if (hour < 0){
            hour += 24;
        }

        bw.write(Integer.toString(hour) + " " + Integer.toString(min));
        bw.flush();
        br.close();
        bw.close();
    }
}
