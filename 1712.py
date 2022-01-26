import sys
input = sys.stdin.readline

A, B, C = list(map(int, input().split()))

temp = C - B
if temp > 0:
    if C < B:
        print(-1)
    else:
        print(int(A // temp + 1))
else:
    print(-1)
