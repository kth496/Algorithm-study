import java.lang.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        class pos {
            int h, r, c;

            public pos(int h_, int r_, int c_) {
                h = h_;
                r = r_;
                c = c_;
            }
        }

        Scanner sc = new Scanner(System.in);
        int C = sc.nextInt();
        int R = sc.nextInt();
        int H = sc.nextInt();
        int[][][] box = new int[H][R][C];
        int[][][] v = new int[H][R][C];
        Queue<pos> q = new LinkedList<>();

        for (int h = 0; h < H; h++) {
            for (int r = 0; r < R; r++) {
                for (int c = 0; c < C; c++) {
                    box[h][r][c] = sc.nextInt();
                    if (box[h][r][c] == 1)
                        q.add(new pos(h, r, c));
                }
            }
        }

        int[] dh = {1, -1, 0, 0, 0, 0};
        int[] dr = {0, 0, 1, -1, 0, 0};
        int[] dc = {0, 0, 0, 0, 1, -1};

        while (!q.isEmpty()) {
            pos tmp = q.poll();
            int h = tmp.h;
            int r = tmp.r;
            int c = tmp.c;
            for (int i = 0; i < 6; i++) {
                int nh = h + dh[i];
                int nr = r + dr[i];
                int nc = c + dc[i];
                if (nh < 0 || nr < 0 || nc < 0 || nh >= H || nr >= R || nc >= C || v[nh][nr][nc] == 1 || box[nh][nr][nc] != 0)
                    continue;
                box[nh][nr][nc] = box[h][r][c] + 1;
                v[nh][nr][nc] = 1;
                q.add(new pos(nh, nr, nc));
            }
        }

        int ans = 0;
        for (int[][] floor : box) {
            for (int[] row : floor) {
                for (int e : row) {
                    if (e == 0) {
                        System.out.println(-1);
                        System.exit(0);
                    } else {
                        ans = Math.max(ans, e);
                    }
                }
            }
        }
        System.out.println(ans - 1);
    }
}
