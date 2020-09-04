import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());


        int ans = 1;
        int[] arr = new int[n + 1];
        for (int i = 2; i < n + 1; i++) {
            if (arr[i] != 0) continue;
            arr[i] = ans;
            ans++;
            for (int j = 2 * i; j < n + 1; j += i) {
                if (arr[j] == 0) {
                    arr[j] = ans;
                    ans++;
                }
            }
        }
        for (int i = 2; i < n + 1; i++) {
            if (arr[i] == k) {
                System.out.println(i);
                break;
            }
        }
    }
}
