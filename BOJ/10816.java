import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        HashMap<Integer, Integer> mp = new HashMap<>();

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            int cur = Integer.parseInt(st.nextToken());
            if (mp.containsKey(cur)) mp.put(cur, mp.get(cur) + 1);
            else mp.put(cur, 1);
        }

        st = new StringTokenizer(br.readLine());
        int M = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++) {
            int cur = Integer.parseInt(st.nextToken());
            if (mp.containsKey(cur)) System.out.print(mp.get(cur) + " ");
            else System.out.print(0 + " ");
        }
        System.out.println();
    }
}
