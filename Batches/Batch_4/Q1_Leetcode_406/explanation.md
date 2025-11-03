# LeetCode 406 — Queue Reconstruction by Height

## Problem Link
https://leetcode.com/problems/queue-reconstruction-by-height/

---

## Problem Description
You are given an array `people` where each element is a pair `[h, k]`:
- `h`: height of the person
- `k`: number of people in front with height ≥ `h`

Reconstruct the queue so that every person’s `[h, k]` condition is satisfied.

---

## Intuition
Each person’s `k` value depends only on taller or equal height people.  
So we can arrange taller people first — their placement won’t be affected by shorter ones.  
This leads to a greedy approach.

---

## Approaches

### 1. Non-Optimal (Brute Force / Ascending Sort)
1. Sort the array by **height ascending** and then by **k ascending**.
2. Initialize an empty queue of size `n`.
3. For each person in the sorted list:
   - Count positions in the queue that are either empty or contain taller people.
   - Once the count equals that person’s `k`, place them in that position.
4. Continue until all people are placed.

Example walkthrough:
Input: [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]  
Sorted (ascending): [[4,4],[5,0],[5,2],[6,1],[7,0],[7,1]]  
Final queue built by scanning positions one by one.

**Complexity:** O(n²) (due to scanning for each placement).

---

### 2. Optimal Greedy Approach (Descending Sort)
1. Sort people by:
   - Height descending
   - `k` ascending if heights are equal

Example after sorting:
[[7,0],[7,1],[6,1],[5,0],[5,2],[4,4]]

2. Use a list and insert each person at index = `k`.

Example walkthrough:
Input: [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]  
Sorted: [[7,0],[7,1],[6,1],[5,0],[5,2],[4,4]]

[] → [[7,0]]  
→ [[7,0],[7,1]]  
→ [[7,0],[6,1],[7,1]]  
→ [[5,0],[7,0],[6,1],[7,1]]  
→ [[5,0],[7,0],[5,2],[6,1],[7,1]]  
→ [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]

Final Queue: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]

---

## Complexity
| Step | Time | Space |
|------|------|-------|
| Sorting | O(n log n) | O(1) |
| Insertions | O(n²) | O(n) |
| Total | O(n²) | O(n) |

---

## Key Idea
Placing taller people first ensures correctness.  
Since shorter people do not affect the position of taller ones, inserting each at index `k` guarantees that `k` taller or equal people are ahead.

---

## Algorithm Steps

### Brute Force
1. Sort people by height ascending, then k ascending.  
2. Initialize empty result array of size n.  
3. For each person:
   - Scan positions and count available or taller spots.
   - Place person when count == k.  
4. Return final queue.

### Greedy
1. Sort people by height descending, then k ascending.  
2. Initialize empty list.  
3. For each person:
   - Insert at position k.  
4. Return list as array.

---

## Comparison
| Approach | Sorting | Placement | Time | Efficient? |
|-----------|----------|------------|------|-------------|
| Brute Force | Ascending | Count spaces | O(n²) | No |
| Greedy | Descending | Insert by k | O(n²) | Yes |
