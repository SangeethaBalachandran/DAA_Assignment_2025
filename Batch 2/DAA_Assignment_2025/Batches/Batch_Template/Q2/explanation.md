# Skyline Problem (LeetCode 218)

## Problem Statement

You are given a list of buildings in the form `buildings = [ [left, right, height], ... ]`.

Each building is represented by:

- **left**: x-coordinate where the building starts  
- **right**: x-coordinate where the building ends  
- **height**: the building’s height  

The task is to output the **skyline**, which is the outer contour formed by all the buildings viewed from a distance.

---

## Approach: Sweep Line Algorithm with Max Heap

### Intuition

We process all building edges (start and end points) in sorted order of their x-coordinates.  
A **max-heap** keeps track of the current active building heights.

- When a building **starts**, add its height to the heap.  
- When it **ends**, remove its height.  
- If the tallest height changes, that means the skyline has a new point.

---

## Algorithm Steps

### 1. Split Building Edges
For each building `[L, R, H]`, add `(L, -H)` for the start and `(R, H)` for the end.  
Negative height ensures starts come before ends at the same x.

### 2. Sort All Edges
Sort by x-coordinate.  
If x is the same:
- Start edges come before end edges.
- Higher start processed first.

### 3. Initialize Max Heap
Use a priority queue (**max-heap**) to store current active heights.  
Start with ground level (0).

### 4. Process Each Edge
- If it’s a start edge, add the height to the heap.  
- If it’s an end edge, remove the height from the heap.  
- Let `currMax = pq.peek()` (current tallest height).

### 5. Check for Skyline Change
If `currMax != prevMax`, a skyline change occurred.  
Add `[x, currMax]` to the result and update `prevMax = currMax`.

### 6. Return the Result
The result list now contains all skyline points.

---

## Time and Space Complexity

| Operation | Complexity |
|------------|-------------|
| Creating edges | O(N) |
| Sorting edges | O(N log N) |
| Processing edges (heap add/remove) | O(N log N) |
| **Total Time** | **O(N log N)** |
| **Space Complexity** | **O(N)** |

---

## Java Implementation

```java
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