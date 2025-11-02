# Majority Element Problem (Boyer-Moore Voting Algorithm)

## 🧩 Problem Statement
Given an array `arr[]` of size `n`, find the element that appears more than `n/2` times (the majority element).  
It is guaranteed that a majority element always exists.

---

## 💡 Approach: Boyer–Moore Voting Algorithm

### Intuition
The majority element appears more than half the time, meaning it can *"cancel out"* all other elements.  
We use a counter that increases for the same element and decreases for different ones.  
When the counter reaches 0, we pick the next element as a new candidate.

---

## 🧠 Algorithm Steps
1. Initialize `count = 1` and `element = arr[0]`.
2. Traverse the array from index `1` to `n-1`:
   - If `count == 0`, set `element = arr[i]` and `count = 1`.
   - Else if `arr[i] == element`, increment `count`.
   - Else, decrement `count`.
3. Return `element` at the end (the majority element).

---

## ⏱️ Time and Space Complexity

| Operation         | Complexity |
|-------------------|-------------|
| Traversing Array  | **O(N)**    |
| Extra Space       | **O(1)**    |

---

## 🧮 Java Implementation

```java
import java.util.Scanner;

public class MajorityElement {

    public static int MajorityElementFinder(int[] arr) {
        int n = arr.length;
        int count = 1, element = arr[0];
        for (int i = 1; i < n; i++) {
            if (count == 0) {
                element = arr[i];
                count = 1;
            } else if (arr[i] == element) {
                count++;
            } else {
                count--;
            }
        }
        return element;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the size of the array: ");
        int n = sc.nextInt();
        int[] arr = new int[n];

        System.out.println("Enter " + n + " elements:");
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        int majority = MajorityElementFinder(arr);
        System.out.println("Majority Element: " + majority);

        sc.close();
    }
}