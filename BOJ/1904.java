
import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());

        ArrayList<Integer> arr = new ArrayList<>();
        arr.add(0);
        arr.add(1);
        arr.add(2);
        for (int i = 3; i <= n; i++) {
            arr.add((arr.get(i - 1) + arr.get(i - 2)) % 15746);
        }
        System.out.println(arr.get(n) % 15746);


/*        Queue<String> q = new LinkedList<>();
        q.add("");
        int ans = 0;
        while (!q.isEmpty()) {
            String cur = q.poll();
            if (cur.length() == n) {
                ans++;
                continue;
            }
            if (n - cur.length() > 1) {
                q.add(cur + "00");
            }
            q.add(cur + "1");
        }
        System.out.println(ans);*/
    }
}
/*
* 처음에 큐를 이용해서 모든 경우 계산을 시도
* 최대입력(N = 100만)에서 시간초과됨
* dp 배열을 그려보며 계산해보니 피보나치수열과 일치
* */
