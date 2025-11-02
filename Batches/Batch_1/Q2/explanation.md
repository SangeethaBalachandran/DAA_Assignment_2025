# Problem: Reverse Pairs

### **Problem Link:** [LeetCode](https://leetcode.com/problems/reverse-pairs/)

---

## Algorithm / Approach Explanation

We are asked to count the number of **reverse pairs** in an array.  
A reverse pair is defined as a pair of indices `(i, j)` such that:

`i < j and nums[i] > 2 * nums[j]`


A brute-force approach would take **O(n²)** time, checking every possible pair — which is inefficient for large inputs.

To optimize this, we use a **modified merge sort** approach that counts reverse pairs during the merging process in **O(n log n)** time.

### **Core Idea:**

- In merge sort, both halves of the array are **sorted** before merging.
- For each element in the left half (`nums[i]`), we count how many elements in the right half (`nums[j]`) satisfy the condition:

  **nums[i] > 2 * nums[j]**

- Since both halves are sorted, we can count these efficiently using a **two-pointer technique** during merge.

---

## **Algorithm Steps**

1. **Divide** the array into two halves using merge sort.
2. **Recursively count** reverse pairs in the left and right halves.
3. **Count cross pairs** between the two halves:
   - Initialize a pointer `j` for the right half.
   - For each element `nums[i]` in the left half:
     - Move `j` forward while `nums[i] > 2 * nums[j]`.
     - Add `(j - (mid + 1))` to the count.
4. **Merge** the two halves in sorted order to maintain the sorted property.
5. Return the total count of reverse pairs.

---

## **Example and Illustration**

### Example Input
```
5
1 3 2 3 1
```

### Step-by-Step Illustration

| Step | Left Half | Right Half | Merging Process | Reverse Pairs Count |
|------|------------|-------------|-----------------|---------------------|
| 1 | [1, 3, 2] | [3, 1] | Split into halves | 0 |
| 2 | [1, 3] + [2] | [3] + [1] | Sort each half | 0 |
| 3 | ||Merge [3] & [1] <br> One reverse pair (3, 1) |1|
| 4 | ||Merge [1, 3, 2] & [1, 3] <br> Compare across halves: <br> - (3, 1) → valid <br> - (3, 1) → valid | 2

### Example Output
```
2
```

---

## **Time Complexity**
- **O(n log n)** — The counting and merging happen in logarithmic recursive depth.
- **O(n)** — Merging each level takes linear time.

## **Space Complexity**
- **O(n)** — Temporary arrays are used during the merge process.

