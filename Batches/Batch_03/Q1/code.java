package Batches.Batch_05.Q1;

class code {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int n = gas.length;       // Number of gas stations
        int gass = 0;             // Total gas available
        int costs = 0;            // Total cost to travel around

        // Step 1: Calculate total gas and total cost
        for (int i = 0; i < n; i++) {
            gass += gas[i];
            costs += cost[i];
        }

        // If total cost is greater than total gas, completing the circuit is impossible
        if (costs > gass) return -1;

        int index = 0;  // Candidate starting station
        int cur = 0;    // Current fuel balance while traveling

        // Step 2: Try to find the valid starting station
        for (int i = 0; i < n; i++) {
            cur += gas[i] - cost[i];  // Update fuel balance after visiting station i

            // If fuel balance drops below 0, we cannot start from this or any previous station
            if (cur < 0) {
                cur = 0;              // Reset current fuel
                index = (i + 1) % n;  // Try next station as the new start point
            }
        }

        // Step 3: Return the valid starting index
        return index;
    }
}

