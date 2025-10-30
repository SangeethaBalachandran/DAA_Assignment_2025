## **Problem Definition**

A **peak element** in an array `arr` is an element that is **strictly greater** than both of its neighbors.  
  Formally, for any index `i`, an element `arr[i]` is a peak if:

arr\[i−1\]\<arr\[i\]\>arr\[i+1\]arr\[i-1\] \< arr\[i\] \> arr\[i+1\]arr\[i−1\]\<arr\[i\]\>arr\[i+1\]

The goal is to find **any one peak element index**.

Example:  
  arr \= \[1, 2, 3, 1\] → Output \= 2 (since `3` is greater than both its neighbors `2` and `1`).

## **1\. Brute Force Approach**

### **Algorithm**

`class Solution:`

	`def findPeakElement(self, arr):`

    	`n=len(arr)`

    	`if n==1:`

        	`return 0`

    	`if arr[0]>arr[1]:`

        	`return 0`

    	`for i in range(1,n-1):`

        	`if arr[i]>arr[i-1] and arr[i]>arr[i+1]:`

            	`return i`

    	`if arr[-1]>arr[-2]:`

        	`return n-1`

    	`return -1` 

**Step-by-Step Explanation**

**1.Checking if there is only one element**  
  `if n==1:`

	`return 0`

If the array length is 1, that element itself is a peak since there are no neighbors to compare with.

**2.Checking the first element**  
  `if arr[0]>arr[1]:`

	`return 0`

If the first element is greater than the second, it qualifies as a peak and index `0` is returned.

**3.Iterating through middle elements**  
  `for i in range(1, n-1):`

	`if arr[i]>arr[i-1] and arr[i]>arr[i+1]:`

    	`return i`

For each element (from index `1` to `n-2`), the algorithm checks if it is greater than both its left and right neighbors.

Once such an element is found, its index is immediately returned.

**4.Checking the last element**  
  `if arr[-1]>arr[-2]:`

	`return n-1`

If no middle element is a peak, the algorithm checks whether the last element is greater than its left neighbor. If yes, its index is returned.

**5.Fallback condition**

  `return -1`

This line acts as a safeguard. However, according to problem constraints, there is always at least one peak, so this line should theoretically never execute.

**Complexity Analysis**

●      **Time Complexity:**  
  The loop at most visits each element once, making it **O(n)**.  
  Every comparison operation (`>`) takes constant time.  
●      **Space Complexity:**  
  No additional data structures are used apart from a few variables, so the space complexity is **O(1)**.

### **Observation**

While this brute force approach is simple and easy to understand, it becomes inefficient for very large arrays because it checks each element one by one.

## **2\. Optimized Approach (Binary Search)**

### **Algorithm**

`class Solution:`

	`def findPeakElement(self, arr):`

    	`start=1`

    	`end=len(arr)-2`

    	`while start<=end:`

        	`mid=start+(end-start)//2`

        	`if arr[mid-1]<arr[mid] and arr[mid]>arr[mid+1]: return mid`

        	`if arr[mid]<arr[mid+1]:start=mid+1`

        	`else:`

            	`end=mid-1`

    	`if len(arr)==1 or arr[0]>arr[1]:`

        	`return 0`

    	`if arr[-1]>arr[-2]:`

        	`return len(arr)-1`

    	`return -1`

### **Step-by-Step Explanation**

**1.Initialization**  
  `start=1`

`end=len(arr)-2`

The search begins between the first and last valid middle indices.  
 The endpoints are checked separately later to avoid index errors.

**2.Binary Search Iteration**  
  `while start<=end:`

	`mid=start+(end-start)//2`

At each iteration, a midpoint is calculated.

Instead of scanning sequentially, the array is divided in half during each step, similar to binary search.

**3.Checking for a Peak at Mid**  
  `if arr[mid-1]<arr[mid] and arr[mid]>arr[mid+1]:`

	`return mid`

If the middle element is greater than both its neighbors, it is a peak.

**4.Deciding the Search Direction**  
  `if arr[mid]<arr[mid+1]: start=mid+1`

`else:end=mid-1`

If the right neighbor is larger, the peak must lie on the right side (since the slope is increasing).  
 Otherwise, the peak lies on the left side, and `end` is moved leftward.

**5.Boundary Checks**  
  `if len(arr)==1 or arr[0]>arr[1]:`

	`return 0`

`if arr[-1]>arr[-2]:`

	`return len(arr)-1`

These conditions handle single-element arrays and potential peaks at the boundaries.

###  

### **Complexity Analysis**

●      **Time Complexity:**  
  Since the search range is divided by half in every iteration, the time complexity is **O(log n)**.  
●      **Space Complexity:**  
  Only constant variables are used (`start`, `end`, `mid`), resulting in **O(1)** space usage.

## **3\. Comparative Analysis**

| Aspect | Brute Force Approach | Optimized (Binary Search) Approach |
| ----- | ----- | ----- |
| **Technique Used** | Sequential linear scan | Binary search on slope direction |
| **Time Complexity** | O(n) | O(log n) |
| **Space Complexity** | O(1) | O(1) |
| **Best Case** | Early peak found | Early peak found |
| **Worst Case** | Needs full traversal | Logarithmic reduction per step |
| **Scalability** | Inefficient for large n | Highly efficient for large n |

## **4\. Conclusion**

The **brute force approach** is simple and intuitive but requires linear traversal of the array, resulting in **O(n)** time complexity.The **optimized binary search approach**, however, leverages the structure of the array to iteratively narrow the search region based on slope direction, achieving **O(log n)** time complexity. This reduces computational effort significantly, especially for large datasets, and is therefore the preferred method in performance-critical applications.

