import java.util.*;
import java.io.*;

public class Main {
    static long sum(long x) {
        return x * (x + 1) / 2;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        long N = Long.parseLong(st.nextToken());

        long i = 1;
        while (true) {
            if (sum(i) <= N && N < (sum(i + 1))) {
                System.out.println(i);
                System.exit(0);
            }
            i++;
        }
    }
}
