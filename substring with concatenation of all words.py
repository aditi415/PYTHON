def findSubstring(s, words):
    wl = len(words[0])
    total_len = wl * len(words)

    word_count = {}
    for w in words:
        word_count[w] = word_count.get(w, 0) + 1

    result = []

    for i in range(len(s) - total_len + 1):
        seen = {}
        for j in range(0, total_len, wl):
            word = s[i+j:i+j+wl]
            seen[word] = seen.get(word, 0) + 1

        if seen == word_count:
            result.append(i)

    return result


# 🔹 USER INPUT
if __name__ == "__main__":
    s = input("Enter string: ")

    n = int(input("Enter number of words: "))
    words = []

    print("Enter words:")
    for _ in range(n):
        words.append(input().strip())

    result = findSubstring(s, words)

    print("\nStarting indices:", result)
