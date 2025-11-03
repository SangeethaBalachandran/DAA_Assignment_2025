
# 🧩 Question 2: Merge K Sorted Lists (LeetCode #23)

## 🔗 Problem Link  
[LeetCode #23 - Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)

---

## 🧠 Problem Statement  
You are given an array of `k` linked-lists, each of which is sorted in ascending order.  
Your task is to **merge all the linked lists into one sorted linked list** and return it.

---

## ⚙️ Algorithm / Approach — Min Heap (Priority Queue)

### 🪄 Idea  
Instead of merging lists one by one, use a **Min Heap** to always pick the smallest current node among all list heads efficiently.

### 🧩 Steps
1. Initialize an empty **min heap**.  
2. Insert the head of each non-empty linked list into the heap.  
   Each entry in the heap is a tuple `(node value, unique id, node reference)` to avoid comparison errors.
3. Create a **dummy head node** for the merged linked list.
4. Repeatedly extract the smallest element from the heap:
   - Append it to the merged linked list.
   - If that node has a next node, push it into the heap.
5. Continue until the heap becomes empty.
6. Return the merged list starting from `dummy.next`.

---

## 🧮 Example

### Input:
lists = [[1,4,5], [1,3,4], [2,6]]

shell
Copy code

### Output:
1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6

yaml
Copy code

---

## ⏱️ Time Complexity  
- Building heap: **O(k)**  
- Each insertion/extraction: **O(log k)**  
- Total nodes processed: **N**  
✅ **Overall Time Complexity:** `O(N log k)`

## 💾 Space Complexity  
- Heap stores up to `k` nodes → **O(k)**  
✅ **Total Space Complexity:** `O(k)`

---

## 🧠 Approach Category  
**Greedy + Partial Divide and Conquer** using **Min Heap (Priority Queue)**
