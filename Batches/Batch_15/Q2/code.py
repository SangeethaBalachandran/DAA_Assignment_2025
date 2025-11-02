def findAllConcatenatedWords(words):
    word_set = set(words)
    result = []
    for word in words:
        if not word:
            continue
        word_set.remove(word)  
        n = len(word)
        dp = [False] * (n + 1)
        dp[0] = True 
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and word[j:i] in word_set:
                    dp[i] = True
                    break  
        if dp[n]:
            result.append(word)
        word_set.add(word)
    return result

words = ["cat", "cats", "dog", "catsdog"]
print(findAllConcatenatedWords(words))

