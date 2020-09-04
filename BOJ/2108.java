import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        // 산술평균
        int sum = 0, ret;
        for (int i = 0; i < N; i++) {
            sum += arr[i];
        }

        float tmp = (float)Math.abs(sum) / N;
        ret = Math.round(tmp);
        if (sum < 0) System.out.println(-ret);
        else System.out.println(ret);

        Arrays.sort(arr);
        // 중앙값
        System.out.println(arr[N / 2]);

        // 최빈값
        // preq은 (빈도, 숫자) 로 되어있음.
        HashMap<Integer, Integer> mp = new HashMap<>();
        ArrayList<Integer> num = new ArrayList<>();
        for (int e : arr) {
            if (mp.containsKey(e)) mp.put(e, mp.get(e) + 1);
            else {
                num.add(e);
                mp.put(e, 1);
            }
        }

        ArrayList<int[]> preq = new ArrayList<>();
        for (int e : num) {
            preq.add(new int[]{mp.get(e), e});
        }

        Collections.sort(preq, (x, y) -> {
            if (x[0] == y[0]) return Integer.compare(x[1], y[1]);
            else return Integer.compare(y[0], x[0]);
        });

        if (preq.size() > 1 && (preq.get(0)[0] == preq.get(1)[0]))
            System.out.println(preq.get(1)[1]);
        else
            System.out.println(preq.get(0)[1]);

        // 범위
        System.out.println(arr[N - 1] - arr[0]);
    }
}

/*
* 자바 round사용 시 주의할 점
*         float tmp = (float)Math.abs(sum) / N;
*         ret = Math.round(tmp);
* 위 소스에서 tmp를 계산할 때, (float) 강제 형변환을 하지 않으면 tmp에서 소수점이 절삭됨
* 그래서 round가 의도한대로 동작하지 않는다.
*/
