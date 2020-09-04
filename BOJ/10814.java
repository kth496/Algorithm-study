import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());

        String[][] data = new String[N][2];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            String age = st.nextToken();
            String name = st.nextToken();
            data[i][0] = age;
            data[i][1] = name;
        }

        Arrays.sort(data, Comparator.comparingInt(o -> Integer.parseInt(o[0])));

        for (int i = 0; i < N; i++)
            System.out.println(data[i][0] + " " + data[i][1]);
    }
}
/*
 * 22라인에서 나이별로 비교할 때, Arrays.sort 메서드에 Integer.compare 사용하는 람다식을 전달했다.
 * comparingInt를 사용하는 버전이 더 깔끔해진다.
*/
