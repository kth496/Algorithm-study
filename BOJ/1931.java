import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        ArrayList<int[]> arr = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int fr = Integer.parseInt(st.nextToken());
            int to = Integer.parseInt(st.nextToken());
            arr.add(new int[]{fr, to});
        }

//        Collections.sort(arr, Comparator.comparingInt(o -> o[0]));
//        Collections.sort(arr, Comparator.comparingInt(o -> o[1]));

        Collections.sort(arr, (o1, o2) -> {
            if (o1[1] == o2[1]) return Integer.compare(o1[0], o2[0]);
            else return Integer.compare(o1[1], o2[1]);
        });

        int cur = 0;
        int ans = 0;

        for (int[] e : arr) {
            if (e[0] >= cur) {
                ans++;
                cur = e[1];
            }
        }
        System.out.println(ans);
    }
}
