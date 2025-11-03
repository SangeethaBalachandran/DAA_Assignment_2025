Program Link:
https://www.hackerrank.com/challenges/unbounded-knapsack/problem

Algorithm:
1.Sort items in descending order based on their value-to-weight ratio.
2.Initialize a queue and add a root node representing no items chosen yet.
3.Set maximum profit to 0.
4.While the queue is not empty:
    Remove the front node 𝑢 from the queue.
    If 𝑢 corresponds to having considered all items, skip to the next iteration.
    Create a child node 𝑣 by including the next item:
      Update profit and weight.
      If weight is under capacity and profit is greater than current max, update max profit.
      Calculate an upper bound on possible profit from this node.
      If this bound is better than current max profit, add the node 𝑣 to the queue.
    Create another child node 𝑣 by excluding the next item:
      Keep profit and weight unchanged.
      Calculate an upper bound.
      If this bound is better than current max profit, add the node 𝑣 to the queue.
5.After processing all nodes, the maximum profit recorded is the optimal knapsack solution.

Time Complexity:
    In the worst case, the branch and bound algorithm explores all possible subsets
    Time Complexity = O(2^N)

Space Complexity:
    maximum depth=N(number of nodes)
    Space Complexity = O(2^N)


Sample Input & Output:

Input:                                                                  Output: 
W = 4,                                                                  3
profit[] = [1, 2, 3], 
weight[] = [4, 5, 1]


   


