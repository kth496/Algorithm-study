import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();
        long[] data = new long[N];
        for (int i = 0; i < N; i++) {
            data[i] = sc.nextInt();
        }
        Arrays.sort(data);

        long high = data[N - 1], low = 1;

        long ans = 0;
        while (low <= high) {
            long mid = (low + high) / 2;
            int temp = 0;
            for (int i = 0; i < N; ++i)
                temp += data[i] / mid;

            if (temp >= K) {
                ans = mid;
                low = mid + 1;
            }
            else
                high = mid - 1;
        }
        System.out.println(ans);
    }
}
