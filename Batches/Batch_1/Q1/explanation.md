# Problem: Count of Smaller Numbers After Self

### **Problem Link:** [LeetCode](https://leetcode.com/problems/count-of-smaller-numbers-after-self/)

---

## Algorithm / Approach Explanation

We are asked to find, for each number in an array, **how many smaller numbers appear after it**.  
A brute-force approach would take **O(n²)** time by comparing each element with all the ones after it, which is inefficient.

Hence, we use a **modified merge sort** algorithm to achieve **O(n log n)** time complexity.

### **Core Idea:**

- During the merge step of merge sort, the two halves (`left` and `right`) are already sorted.
- When we pick an element from the left half (`left[i]`) to merge:
  - All elements from the right half that have been merged **before** this element (`right[0..j-1]`) are **smaller** than it.
  - Thus, we can directly **add `j` to the count** of smaller numbers after `left[i]`.

This way, the merge process simultaneously **sorts** and **counts smaller elements**.

---

## **Algorithm Steps**

1. Create a list of tuples: `(value, original_index)` for tracking the position of each number.
2. Perform merge sort on this list:
   - Sort the left and right halves recursively.
   - During merging:
     - If `left[i] <= right[j]`, it means `left[i]` comes before all smaller elements from the right half.
     - So, increment the count for `left[i]` by `j` (the number of smaller elements seen so far).
3. After sorting and merging, the `counts` list will contain the number of smaller elements to the right of each number.

---

## **Example and Illustration**

### Example Input
```
5
5 2 6 1 3
```

### Step-by-Step Illustration

| Step | Left Half | Right Half | Merging Process | Counts |
|------|------------|-------------|-----------------|---------|
| 1 | [5, 2] | [6, 1, 3] | Split into halves | [0, 0, 0, 0, 0] |
| 2 | [5] + [2] | [6] + [1, 3] | Sort each half | [0, 0, 0, 0, 0] |
| 3 | Merge [5] & [2] | Merge [1] & [3] | Count smaller elements | [1, 0, 0, 0, 0] |
| 4 || Merge [2, 5] & [1, 3, 6] | During merging: <br> - 5 sees 3 smaller <br> - 2 sees 1 smaller <br> - 6 sees 2 smaller | [3, 1, 2, 0, 0] |

### Example Output
```
3 1 2 0 0
```

---

## **Time Complexity**
- **O(n log n)** — Each merge step takes O(n), and there are log n levels of recursion.

## **Space Complexity**
- **O(n)** — Additional space is used for temporary merged arrays.

