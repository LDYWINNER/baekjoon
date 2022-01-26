import sys
input = sys.stdin.readline

N = int(input())

for i in range(N // 5, 0, -1):
    if (N - (i * 5)) % 3 == 0:
        N -= i * 5
        print(i + N // 3)
        break
else:
    if N % 3 == 0:
        print(N // 3)
    else:
        print(-1)

