import java.util.*;
import java.io.*;

class Solution {
    public int solution(int cacheSize, String[] cities) {
        int answer = 0;
        if (cacheSize == 0) return cities.length * 5;
        LinkedHashMap<String, Integer> LRU = new LinkedHashMap<>();

        for (String s : cities) {
            String city = s.toUpperCase();

            if (LRU.remove(city, 1)) {
                LRU.put(city, 1);
                answer += 1;
            } else {
                int size = LRU.size();
                if (size == cacheSize) {
                    String first = LRU.keySet().iterator().next();
                    LRU.remove(first, 1);
                }
                LRU.put(city, 1);
                answer += 5;
            }
        }
        
        return answer;
    }
}
