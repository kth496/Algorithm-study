import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[] arr = new int[N];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++)
            arr[i] = Integer.parseInt(st.nextToken());

        Arrays.sort(arr);

        int low = 1, high = arr[N - 1];
        long ans = 0;
        while (low <= high) {
            int mid = (low + high) / 2;
            long temp = 0;
            for (int i = 0; i < N; i++) {
                if (arr[i] - mid > 0) temp += arr[i] - mid;
            }

            if (temp >= M) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        System.out.println(ans);
    }
}

/*
* ans와 temp가 int범위를 넘어설 수 있다는 사실을 까먹고 int로 했다가 한번 틀림
* */
