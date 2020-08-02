import java.util.*;

public class solve_7576 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int m = sc.nextInt();
        int n = sc.nextInt();
        int[] tomato = new int[n * m];
        Queue<Integer> q = new LinkedList<Integer>();
        for (int i = 0; i < n * m; i++) {
            tomato[i] = sc.nextInt();
            if (tomato[i] == 1)
                q.add(i);
        }
        int s = -1;
        while (!q.isEmpty()) {
            int v = q.remove();
            if (v % m != 0 && tomato[v - 1] == 0) {
                tomato[v - 1] = tomato[v] + 1;
                q.add(v - 1);
            }
            if (v % m != m - 1 && tomato[v + 1] == 0) {
                tomato[v + 1] = tomato[v] + 1;
                q.add(v + 1);
            }
            if (v + m < n * m && tomato[v + m] == 0) {
                tomato[v + m] = tomato[v] + 1;
                q.add(v + m);
            }
            if (v - m >= 0 && tomato[v - m] == 0) {
                tomato[v - m] = tomato[v] + 1;
                q.add(v - m);
            }
            s = tomato[v];
        }
        for (int i = 0; i < n * m; i++) {
            if (tomato[i] == 0) {
                System.out.println(-1);
                break;
            }
            if (i == n * m - 1)
                System.out.println(s - 1);
        }
    }
}