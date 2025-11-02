package Batches.Batch_05.Q2;
import java.util.*;

class code {
    public int minRefuelStops(int target, int startFuel, int[][] stations) {
        int n = stations.length;
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> b[1] - a[1]);
        
        int refill = 0, i = 0;
        int distance = startFuel;

        while (distance < target) {
            // Add all reachable stations to max-heap
            while (i < n && distance >= stations[i][0]) {
                pq.offer(stations[i]);
                i++;
            }

  
 // If no reachable station and not at target
            if (pq.isEmpty()) return -1;

            // Refuel from the station with the maximum fuel
            distance += pq.remove()[1];
            refill++;
        }

        return refill;
    }
}
