import java.util.*;
import java.io.*;

public class Main {
    private static int INF = 987654321;
    private static int N;
    private static int M;
    private static int[][] arr;

    static void floyd() {
        for (int k = 0; k < N + 1; k++) {
            for (int i = 0; i < N + 1; i++) {
                for (int j = 0; j < N + 1; j++) {
                    arr[i][j] = Math.min(arr[i][j], arr[i][k] + arr[k][j]);
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());

        /* 입력 받아서 인접행렬 세팅하기 */
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        arr = new int[N + 1][N + 1];

        for (int i = 0; i < N + 1; i++) {
            for (int j = 0; j < N + 1; j++) {
                if (i == j) arr[i][j] = 0;
                else arr[i][j] = INF;
            }
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int ed = Integer.parseInt(st.nextToken());
            arr[s][ed] = arr[ed][s] = 1;
        }
        /* 세팅 끝 */

        /* 플로이드-워셜 알고리즘 적용 */
        floyd();

        /* 정답 계산 및 출력*/
        int ans = -1;
        int KB = INF;
        for (int i = 1; i < N+1; i++) {
            int cur = 0;
            for (int j = 1; j < N+1; j++) {
                cur += arr[i][j];
            }
            if (KB > cur) {
                ans = i;
                KB = cur;
            }
        }
        System.out.println(ans);
    }
}
