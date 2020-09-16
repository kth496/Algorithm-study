import java.util.*;
import java.io.*;

class pair {
    public int x;
    public int y;

    pair(int x_, int y_) {
        x = x_;
        y = y_;
    }
}

public class Main {

    public static final int INF = 987654321;

    static void floyd(int[][] board) {
        int n = board[0].length;
        for (int k = 1; k < n; k++) {
            for (int i = 1; i < n; i++) {
                for (int j = 1; j < n; j++) {
                    if (i == j) board[i][j] = 0;
                    else board[i][j] = Math.min(board[i][j], board[i][k] + board[k][j]);
                }
            }
        }
    }

    static int dist(pair a, pair b) {
        return Math.abs(a.x - b.x) + Math.abs(a.y - b.y);
    }

    public static void main(String[] args) throws IOException {
        StringBuilder sb = new StringBuilder();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        int tc = Integer.parseInt(st.nextToken());
        for (int i = 0; i < tc; i++) {
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken()) + 2;

            int[][] board = new int[n + 1][n + 1];
            for (int j = 0; j < n + 1; j++) {
                for (int k = 0; k < n + 1; k++) {
                    board[j][k] = INF;
                }
            }

            // 1에서 출발, n에서 도착
            ArrayList<pair> store = new ArrayList<>();
            for (int j = 1; j < n + 1; j++) {
                st = new StringTokenizer(br.readLine());
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());

                pair cur = new pair(x, y);
                store.add(cur);
            }
            for (int j = 1; j < n+1; j++) {
                pair cur = store.get(j-1);
                for (int k = j+1; k < n+1; k++) {
                    pair next = store.get(k-1);
                    int val = dist(cur, next);
                    if (val <= 1000) {
                        board[j][k] = val;
                        board[k][j] = val;
                    }
                }
            }



            floyd(board);

            if (board[1][n] == INF) sb.append("sad\n");
            else sb.append("happy\n");
        }
        System.out.println(sb);
    }
}
