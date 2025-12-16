from collections import deque

def findLadders(beginWord, endWord, wordList):
    wordSet = set(wordList)
    queue = deque([[beginWord]])
    result = []
    visited = set()
    found = False

    while queue and not found:
        level_visited = set()

        for _ in range(len(queue)):
            path = queue.popleft()
            word = path[-1]

            if word == endWord:
                result.append(path)
                found = True

            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = word[:i] + c + word[i+1:]
                    if newWord in wordSet and newWord not in visited:
                        level_visited.add(newWord)
                        queue.append(path + [newWord])

        visited.update(level_visited)

    return result


# 🔹 USER INPUT PART
if __name__ == "__main__":
    beginWord = input("Enter begin word: ")
    endWord = input("Enter end word: ")

    n = int(input("Enter number of words: "))
    wordList = []

    print("Enter words:")
    for _ in range(n):
        wordList.append(input().strip())

    result = findLadders(beginWord, endWord, wordList)

    if result:
        print("\nShortest Transformation Sequences:")
        for path in result:
            print(path)
    else:
        print("\nNo transformation sequence found")
