import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());

        int[] arr = {0, 64, 32, 16, 8, 4, 2, 1};
        int length = 0;
        int ans = 0;
        for (int i = 1; i < arr.length; i++) {
            if (length + arr[i] <= N) {
                ans += 1;
                length += arr[i];
            }
            if (length == N) break;
        }
        System.out.println(ans);
    }
}

// 파이썬 풀이
// print(bin(int(input()))[2:].count('1'))
