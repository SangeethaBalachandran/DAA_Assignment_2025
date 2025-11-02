**Link:**https://leetcode.com/problems/minimum-number-of-refueling-stops/ 

This is a classic greedy problem:

Always refuel at the station offering the most fuel so far when you're about to run out.



**Algorithm:**



1.Use a max heap to keep track of the fuel at all stations you've passed.

2.Start with your initial startFuel and move forward.

3.For every station within reach (i.e., its position ≤ current fuel), add its fuel to the heap.

4.When you can't move forward anymore:

5.Refuel using the station with the most fuel so far (top of the heap).

6.Increase your stop count.

7.Repeat this until your fuel gets you to or beyond the target.



**INPUT:**

target = 100, startFuel = 10  

stations = \[\[10,60],\[20,30],\[30,30],\[60,40]]



1.Start with fuel = 10

2.Can reach station at 10 → push 60 to heap

3.Can't move further → pop 60 → fuel = 70, stops = 1

4.Now can reach stations at 20, 30, 60 → push 30, 30, 40 → heap = \[40, 30, 30]

5.Still fuel < target → pop 40 → fuel = 110, stops = 2



Reached the target.

**Output: 2**



*Complexity:Greedy + Priority Queue ensures we always choose the optimal refueling option just in time.*



***Time complexity: O(n log n)***

Each station is pushed/popped from the heap at most once.



***Space complexity: O(n)***

Heap may store all stations in the worst case.

