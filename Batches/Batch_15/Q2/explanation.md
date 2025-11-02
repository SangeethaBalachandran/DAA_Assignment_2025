# Concatenated Words Problem Explanation

## Problem Link
[LeetCode #472 - Concatenated Words](https://leetcode.com/problems/concatenated-words/)

---

## Problem Description
You are given a list of words (strings). A **concatenated word** is a word that is formed by concatenating at least **two shorter words** from the same list.

You need to return **all concatenated words** in the given list.

---

##  Algorithm / Approach Explanation

### Idea
For each word, we use **Dynamic Programming (DP)** to check whether it can be constructed by joining other words in the given list.

### Steps

1. **Convert list to a set**
   ```python
   word_set = set(words)
   ```
   This allows O(1) lookup to check if a substring exists in the list.

2. **Iterate through each word**
   For each word, temporarily remove it from the set to avoid using itself in the check.

3. **Initialize a DP array**
   ```python
   dp = [False] * (n + 1)
   dp[0] = True
   ```
   - `dp[i]` means: the substring `word[:i]` can be formed by concatenating words from the set.
   - `dp[0] = True` means an empty string is always valid as a starting point.

4. **Check all substrings**
   For each position `i` in the word, check all `j < i`:
   ```python
   if dp[j] and word[j:i] in word_set:
       dp[i] = True
       break
   ```
   This means if `word[:j]` can be formed and `word[j:i]` is a valid word, then `word[:i]` can also be formed.

5. **Check final condition**
   - If `dp[n]` (where n = len(word)) is `True`, the word can be formed by concatenating other words.
   - Add it to the result list.

6. **Add the word back**
   Reinsert the word into the set for further checks.

---

## Example

### Example 1
**Input:**
```python
words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatsdogcat"]
print(findAllConcatenatedWords(words))
```

**Output:**
```
["catsdogcats", "dogcatsdog", "ratcatsdogcat"]
```

**Explanation:**
- `catsdogcats` = "cats" + "dog" + "cats"
- `dogcatsdog` = "dog" + "cats" + "dog"
- `ratcatsdogcat` = "rat" + "cats" + "dog" + "cat"

---

## ⏱️ Time and Space Complexity

| Complexity | Description |
|-------------|--------------|
| **Time:**  | O(N * L²), where N = number of words, L = average word length (each substring check takes O(L²)) |
| **Space:** | O(L), for the DP array per word |

---

## Summary

| Step | Purpose |
|------|----------|
| Convert to set | Enables fast substring lookups |
| DP table | Tracks valid substring combinations |
| Remove & re-add | Avoids using the word itself |
| Collect valid words | Build final concatenated list |
