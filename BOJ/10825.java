import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());

        String[][] arr = new String[n][4];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            String name = st.nextToken();
            String k = st.nextToken();
            String e = st.nextToken();
            String m = st.nextToken();
            arr[i] = new String[]{name, k, e, m};
        }

        Arrays.sort(arr, (String[] o1, String[] o2) -> {
            if (!o1[1].equals(o2[1])) return Integer.compare(Integer.parseInt(o2[1]), Integer.parseInt(o1[1]));
            else if (!o1[2].equals(o2[2])) return Integer.compare(Integer.parseInt(o1[2]), Integer.parseInt(o2[2]));
            else if (!o1[3].equals(o2[3])) return Integer.compare(Integer.parseInt(o2[3]), Integer.parseInt(o1[3]));
            else return o1[0].compareTo(o2[0]);
        });

        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i][0]);
        }
    }
}
