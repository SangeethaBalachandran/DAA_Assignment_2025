def leastInterval(tasks, n):
    freq = {}
    for t in tasks:
        freq[t] = freq.get(t, 0) + 1
    max_freq = max(freq.values())
    count_max = 0
    for v in freq.values():
        if v == max_freq:
            count_max += 1
    total_time = (max_freq - 1) * (n + 1) + count_max
    return max(len(tasks), total_time)


tasks = ["A", "A", "A", "B", "B", "B"]
n = 0
print(leastInterval(tasks, n))
