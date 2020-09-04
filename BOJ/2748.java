import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        ArrayList<Long> arr = new ArrayList<>();
        arr.add((long) 0);
        arr.add((long) 1);
        for (int i = 1; i < N; i++) {
            arr.add(arr.get(i) + arr.get(i - 1));
        }
        System.out.println(arr.get(N));
    }
}
