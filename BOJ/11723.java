import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());

        Set<Integer> s = new HashSet<>();
        StringBuilder ans = new StringBuilder();
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            String cmd = st.nextToken();
            int val = 0;
            if (cmd.equals("all") || cmd.equals("empty")) val = 0;
            else val = Integer.parseInt(st.nextToken());
            if (cmd.equals("add"))
                s.add(val);
            else if (cmd.equals("remove"))
                s.remove(val); // remove 연산은 요소가 없을때는 아무런 작동을 하지 않는다. 에러도 안뱉음
            else if (cmd.equals("check")) {
                if (s.contains(val)) ans.append("1\n");
                else ans.append("0\n");
            } else if (cmd.equals("toggle")) {
                if (s.contains(val)) s.remove(val);
                else s.add(val);
            } else if (cmd.equals("all")) {
                s.clear();
                for (int j = 1; j < 21; j++) s.add(j);
            } else {
                s.clear();
            }
        }
        System.out.println(ans);
    }
}
