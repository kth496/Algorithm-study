import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());

            int[] arr = new int[N];
            Queue<Integer> q = new LinkedList<>();
            int[] prior = new int[10];
            int key = 0;
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                int tmp = Integer.parseInt(st.nextToken());
                if (j == M) key = tmp;
                arr[j] = tmp;
                prior[tmp]++;
            }
            arr[M] = -1;

            for (int j = 0; j < N; j++)
                q.add(arr[j]);

            /* 프린터 큐 시뮬레이션 시작 */
            int ans = 0;
            while (true) {
                int cur = q.poll();
                int p;
                if (cur == -1) p = key;
                else p = cur;

                /* 우선순위 검사 */
                boolean flag = false;
                for (int k = p + 1; k < 10; k++) {
                    if (prior[k] != 0) {
                        flag = true;
                        break;
                    }
                }

                // 더 우선순위 높은게 존재
                if (flag) {
                    q.add(cur);
                } else {
                    ans++;
                    prior[p]--;
                    if (cur == -1) {
                        System.out.println(ans);
                        break;
                    }
                }
            }
        }
    }
}
