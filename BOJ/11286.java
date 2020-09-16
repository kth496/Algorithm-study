// 11286
import java.util.*;
import java.io.*;

class Pair implements Comparable<Pair> {
    Integer first, second;

    Pair(int a, int b) {
        first = a;
        second = b;
    }

    @Override
    public int compareTo(Pair o) {
        if (this.first.equals(o.first)) return Integer.compare(this.second, o.second);
        else return Integer.compare(this.first, o.first);
    }

    @Override
    public String toString() {
        return second.toString() + "\n";
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        StringBuilder sb = new StringBuilder();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        PriorityQueue<Pair> pq = new PriorityQueue<>();
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int cmd = Integer.parseInt(st.nextToken());
            if (cmd == 0) {
                if (pq.isEmpty()) sb.append("0\n");
                else {
                    Pair out = pq.poll();
                    sb.append(out.toString());
                }
            } else {
                Pair cur = new Pair(Math.abs(cmd), cmd);
                pq.add(cur);
            }
        }
        System.out.println(sb);
    }
}
