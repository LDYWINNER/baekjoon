import sys

input = sys.stdin.readline

N = int(input())
group_word_count = 0
for i in range(0, N):
    word = str(input().rstrip())

    tempWord = word[0]
    for j in range(0, len(word) - 1):
        if word[j] == word[j + 1]:
            j += 1
        else:
            tempWord += word[j + 1]
    group_word_count += 1
    for k in range(0, len(tempWord)):
        if tempWord.count(tempWord[k]) > 1:
            group_word_count -= 1
            break

print(group_word_count)
