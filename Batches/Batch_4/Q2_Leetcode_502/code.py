# LeetCode 502 — IPO
# Naive and Optimized Solutions

# 🔹 Naive Approach (Brute Force)
def findMaximizedCapital_naive(k, w, profits, capital):
    n = len(profits)
    for _ in range(k):
        max_profit = 0
        index = -1

        for i in range(n):
            if capital[i] <= w and profits[i] > max_profit:
                max_profit = profits[i]
                index = i

        if index == -1:
            break

        w += profits[index]
        profits[index] = 0
        capital[index] = float('inf')

    return w


# 🔹 Optimized Approach (Using Max Heap)
import heapq

def findMaximizedCapital_optimized(k, w, profits, capital):
    projects = sorted(zip(capital, profits))
    max_heap = []
    index = 0

    for _ in range(k):
        while index < len(projects) and projects[index][0] <= w:
            heapq.heappush(max_heap, -projects[index][1])
            index += 1

        if not max_heap:
            break

        w += -heapq.heappop(max_heap)

    return w


# 🔹 Example Run
if __name__ == "__main__":
    profits = [1, 2, 3]
    capital = [0, 1, 1]
    k = 2
    w = 0

    print("Naive Approach Result:", findMaximizedCapital_naive(k, w, profits[:], capital[:]))
    print("Optimized Approach Result:", findMaximizedCapital_optimized(k, w, profits[:], capital[:]))

