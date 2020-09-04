import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        ArrayList<int[]> arr = new ArrayList<>();
        StringTokenizer st;
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            arr.add(new int[]{Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())});
        }

        Collections.sort(arr, (p1, p2) -> {
            if (p1[0] == p2[0]) return Integer.compare(p1[1], p2[1]);
            else return Integer.compare(p1[0], p2[0]);
        });

        for (int[] e : arr) {
            System.out.print(e[0] + " " + e[1]);
            System.out.println();
        }
    }
}
