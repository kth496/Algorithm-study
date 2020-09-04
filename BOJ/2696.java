import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        StringTokenizer st;
        for (int i = 0; i < T; i++) {
            int N = Integer.parseInt(br.readLine());
            ArrayList<Integer> arr = new ArrayList<>();
            ArrayList<Integer> ans = new ArrayList<>();

            int k = 0;
            for (int j = 0; j < N / 10 + 1; j++) {
                st = new StringTokenizer(br.readLine());
                while (st.hasMoreTokens()) {
                    int cur = Integer.parseInt(st.nextToken());
                    arr.add(cur);
                    // 홀수번째마다 출력하기
                    if (k % 2 == 0) {
                        Collections.sort(arr);
                        ans.add(arr.get(k / 2));
                    }
                    k++;
                }
            }

            System.out.println(Math.round((float) N / 2));
            for (int j = 1; j < ans.size() + 1; j++) {
                System.out.print(ans.get(j - 1) + " ");
                if (j % 10 == 0) System.out.println();
            }
            System.out.println();
        }
    }
}

/*
우선순위큐를 써야하는 문제처럼 보이지만, 입력 조건을 바탕으로 시간복잡도를 계산해보면
매 홀수번째 입력마다 ArrayList를 정렬하면서 해결해도 TLE를 받지 않는다.
*/
