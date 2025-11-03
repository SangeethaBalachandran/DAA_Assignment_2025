
// 1️⃣ Non-optimal approach (ascending sort logic)
// 2️⃣ Optimal Greedy approach (descending + LinkedList insertion)

import java.util.*;

class SolutionNonOptimal {
    public int[][] reconstructQueue(int[][] people) {
        int n = people.length;
        int[][] res = new int[n][];
        
        // Step 1: Sort by height ASC, then k ASC
        Arrays.sort(people, (a, b) -> {
            if (a[0] == b[0]) return a[1] - b[1];
            return a[0] - b[0];
        });
        
        // Step 2: Place each person in correct position
        for (int[] p : people) {
            int spaces = p[1];  // number of taller/equal people before
            for (int i = 0; i < n; i++) {
                if (res[i] == null) {
                    if (spaces == 0) {
                        res[i] = p;
                        break;
                    }
                    spaces--;
                } else if (res[i][0] >= p[0]) {
                    spaces--;
                }
            }
        }
        return res;
    }
}

// Optimal approach

class SolutionOptimal {
    public int[][] reconstructQueue(int[][] people) {
        // Step 1: Sort by height DESC, then k ASC
        Arrays.sort(people, (a, b) -> {
            if (a[0] == b[0]) return a[1] - b[1];
            return b[0] - a[0];
        });

        // Step 2: Use LinkedList for efficient insertion
        List<int[]> list = new LinkedList<>();
        for (int[] p : people) {
            list.add(p[1], p); // Insert person at index = k
        }

        // Step 3: Convert to array
        return list.toArray(new int[people.length][]);
    }
}


