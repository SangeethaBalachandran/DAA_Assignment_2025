Problem Link:  
https://www.codechef.com/problems/TADELIVE

Algorithm:
    1. Create a list of all orders with tip values for Andy and Bob, along with the absolute difference between their tips.
    2.Sort the list of orders in descending order of this tip difference.
    3.Initialize counters for the number of orders assigned to Andy and Bob as zero.
    4.For each order in the sorted list:
        I.If Andy’s tip is greater or equal to Bob’s tip and Andy has not reached his order limit, or if Bob has reached his limit, assign the order to Andy and                 update count and total tip.
        II.Otherwise, assign the order to Bob and update count and total tip.
    5.Return the total accumulated tip value.

Time Complexity:
O(N log N)

Space complexity:
Orders list stores N elements → O(N)
A few counters and variables → O(1)
Space Complexity: O(N)

Sample Input & Output:

INPUT:                                            OUTPUT:
5 3 3                                                21
1 2 3 4 5 
5 4 3 2 1
