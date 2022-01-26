import sys

input = sys.stdin.readline

T = int(input())

for i in range(0, T):
    R, S = input().split()
    result = ""
    for j in range(0, len(S)):
        letter = S[j]
        result += (letter * int(R))
    print(result)
