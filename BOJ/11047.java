// 11047
import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        ArrayList<Integer> coins = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int coin = Integer.parseInt(st.nextToken());
            coins.add(coin);
        }

        int ans = 0;
        int i = coins.size() - 1;
        while (K > 0) {
            int coin = coins.get(i);
            if (K >= coin) {
                K -= coin;
                ans++;
            }
            else i--;
        }
        System.out.println(ans);
    }
}
