import java.util.*;
import java.io.*;

public class Main {
    public static long div = 1234567891;

    public static long calc(long c, long i) {
        long ret = c;
        for (int j = 0; j < i; j++) {
            ret = (ret * 31) % div;
        }
        return ret;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        char[] d = st.nextToken().toCharArray();


        long sum = 0;
        for (int i = 0; i < N; i++) {
            long ret = calc(d[i] - 96, i);
            sum += ret;
        }
        System.out.println(sum % div);
    }
}

/*
* 자바에서 char타입을 그냥 숫자처럼 계산하면 아스키코드값으로 다룰 수 있다. C++과 똑같음.
* 이 문제에서 처음에는 수식을 그대로 Math.pow(31, i) 로 구현했었다.
* 생각해보니까 31의 100제곱은 어떤 자료형으로도 오버플로가 난다.
* 그래서 모듈러연산의 특징을 활용해서 해결했다.
* */
