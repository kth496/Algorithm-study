import java.util.*;
import java.io.*;

public class Main {
    private static int R;
    private static int C;
    private static int N;
    private static int ans;

    private static int[] dr = {0, 0, 1, 1};
    private static int[] dc = {0, 1, 0, 1};

    public static void recursive(int n, int r, int c) {
        if (n == 2) {
            for (int i = 0; i < 4; i++) {
                int nr = r + dr[i], nc = c + dc[i];
                ans++;
                if (nr == R && nc == C) {
                    System.out.println(ans - 1);
                    System.exit(0);
                }
            }
            return;
        }
        
        int next = n / 2;

        recursive(next, r, c);
        recursive(next, r, c + next);
        recursive(next, r + next, c);
        recursive(next, r + next, c + next);
        return;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        ans = 0;
        recursive((int) Math.pow(2, N), 0, 0);
    }
}
