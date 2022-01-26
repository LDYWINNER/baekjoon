import sys
input = sys.stdin.readline

s = str(input())
sCount = [-1] * 26
for i in range(0, len(s) - 1):
    temp = ord(s[i]) - 97
    if sCount[temp] == -1:
        sCount[temp] = i

for num in sCount:
    print(str(num), end=" ")
