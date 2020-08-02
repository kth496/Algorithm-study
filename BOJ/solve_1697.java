import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class solve_1697 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        sc.close();
        Queue<Integer> queue = new LinkedList<Integer>();
        int dist[] = new int[100002];
        Arrays.fill(dist, -1);
        dist[n] = 0;
        queue.offer(n);
        while (dist[k] == -1) {
            int temp = queue.poll();
            for (int i = 0; i < 3; i++) {
                int next = 0;
                switch (i) {
                    case 0:
                        next = temp + 1;
                        break;
                    case 1:
                        next = temp - 1;
                        break;
                    case 2:
                        next = temp * 2;
                        break;
                }
                if (next <= 100000 && next >= 0 && dist[next] == -1) {
                    dist[next] = dist[temp] + 1;
                    queue.offer(next);
                }
            }
        }
        System.out.println(dist[k]);
    }
}