 Problem:
 link: https://leetcode.com/problems/gas-station/


 Greedy Idea:

Always refuel at the station with the maximum fuel among all the ones you have already passed when you’re about to run out.

Algorithm:

Use a Max Heap (Priority Queue) to store fuels of all stations within reach.
(In Java, use a max-heap by reversing comparator order)

Start with startFuel and move forward.

For each station whose position ≤ current reachable distance:

Add its fuel amount to the max heap.

If you can’t reach further (no fuel left and target not reached):

Refuel from the station that gives maximum fuel (pop from heap).

Increase the number of refills.

Repeat until:

Your total distance ≥ target → return number of refuels.

Or heap becomes empty → return -1 (can’t reach target).

Dry Run Example:
target = 100, startFuel = 10
stations = [[10,60], [20,30], [30,30], [60,40]]


Step 1:
fuel = 10
Reachable station: 10 → push 60 to heap
heap = [60]

Step 2:
Can’t move further (distance 10 < next station 20)
Pop max fuel = 60 → fuel = 10 + 60 = 70
stops = 1

Step 3:
Now can reach stations 20, 30, 60
Push their fuels → heap = [40, 30, 30]

Step 4:
fuel = 70 < 100 → pop 40 → fuel = 110
stops = 2

Reached target ✅

Output: 2

Time Complexity:

Each station is pushed and popped at most once
→ O(n log n)

Space Complexity:

Heap may store up to all stations
→ O(n)