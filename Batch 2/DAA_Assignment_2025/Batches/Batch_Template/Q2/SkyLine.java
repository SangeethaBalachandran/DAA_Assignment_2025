package DAA_Assignment_2025.Batches.Batch_Template.Q2;

import java.util.*;

public class SkyLine {

    public static List<List<Integer>> getSkyline(int[][] buildings) {
        List<int[]> heights = new ArrayList<>();

        // Step 1: Split building edges
        for (int[] b : buildings) {
            heights.add(new int[]{b[0], -b[2]}); // start edge
            heights.add(new int[]{b[1], b[2]});  // end edge
        }

        // Step 2: Sort edges
        Collections.sort(heights, (a, b) -> {
            if (a[0] != b[0]) return a[0] - b[0];
            return a[1] - b[1];
        });

        // Step 3: Max Heap
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        pq.offer(0);

        List<List<Integer>> result = new ArrayList<>();
        int prevMax = 0;

        // Step 4: Process edges
        for (int[] h : heights) {
            int x = h[0];
            int height = h[1];

            if (height < 0) pq.offer(-height);
            else pq.remove(height);

            int currMax = pq.peek();
            if (currMax != prevMax) {
                result.add(Arrays.asList(x, currMax));
                prevMax = currMax;
            }
        }

        return result;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of buildings: ");
        int n = sc.nextInt();

        int[][] buildings = new int[n][3];
        System.out.println("Enter each building as: left right height");

        for (int i = 0; i < n; i++) {
            buildings[i][0] = sc.nextInt(); // left
            buildings[i][1] = sc.nextInt(); // right
            buildings[i][2] = sc.nextInt(); // height
        }

        // Direct static call — no object created
        List<List<Integer>> skyline = getSkyline(buildings);

        System.out.println("\nSkyline (x, height) points:");
        for (List<Integer> point : skyline) {
            System.out.println(point);
        }

        sc.close();
    }
}