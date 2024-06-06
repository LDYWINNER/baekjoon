import sys
import collections
input = lambda: sys.stdin.readline().rstrip()

word = input().lower()
counts = collections.Counter(word)

if len(counts) == 1:
    print(word[0].upper())
else:
    temp = counts.most_common(2)
    if temp[0][1] == temp[1][1]:
        print("?")
    else:
        print(temp[0][0].upper())

# 메모리는 좀 아꼈는데 시간은 더 늘어남 오히려
