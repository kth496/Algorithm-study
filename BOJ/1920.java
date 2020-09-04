import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        HashMap<Integer, Boolean> mp = new HashMap<>();
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++)
            mp.put(Integer.parseInt((st.nextToken())), true);

        int M = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        while (st.hasMoreTokens()) {
            if (mp.containsKey(Integer.parseInt(st.nextToken()))) System.out.println(1);
            else System.out.println(0);
        }
    }
}

/*
HashSet is Implemented using a hash table. Elements are not ordered.
The add, remove, and contains methods has constant time complexity O(1).

ref : https://dzone.com/articles/hashset-vs-treeset-vs
*/
