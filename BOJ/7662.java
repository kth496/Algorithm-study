import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        int T = Integer.parseInt(st.nextToken());

        for (int i = 0; i < T; i++) {
            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());

            TreeMap<Long, Long> q = new TreeMap<>();

            for (int j = 0; j < N; j++) {
                st = new StringTokenizer(br.readLine());
                String cmd = st.nextToken();
                Long val = Long.parseLong(st.nextToken());

                if (cmd.equals("I")) {
                    if (q.containsKey(val)) q.put(val, q.get(val) + 1);
                    else q.put(val, 1L);
                } else {
                    long key;
                    if(!q.isEmpty()) {
                        if (val == -1) {
                            key = q.firstKey();
                        } else {
                            key = q.lastKey();
                        }
                        if (q.get(key) == 1) q.remove(key);
                        else q.put(key, q.get(key) - 1);
                    }
                }
            }

            if (q.isEmpty()) System.out.println("EMPTY");
            else {
                System.out.println(q.lastKey() + " " + q.firstKey());
            }
        }
    }
}

