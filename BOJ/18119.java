// 18119
import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] memory = new int[N];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            char[] word = st.nextToken().toCharArray();

            for (char w : word) {
                memory[i] |= (1 << (w - 'a'));
            }

        }


        int alphabet = 0x3ffffff; // 26자 표현
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int cmd = Integer.parseInt(st.nextToken());
            char c = st.nextToken().charAt(0);

            if (cmd == 1) {
                alphabet &= ~(1 << (c - 'a'));
            } else {
                alphabet |= (1 << (c - 'a'));
            }

            int ans = 0;
            for (int j = 0; j < N; j++) {
                if ((alphabet&memory[j]) == memory[j]) ans++;
            }
            sb.append(ans + "\n");
        }
        System.out.println(sb);
    }
}
