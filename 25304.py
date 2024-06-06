import sys
input = sys.stdin.readline

X = int(input().rstrip())
N = int(input().rstrip())
total = 0

for i in range(N):
    x, n = map(int, input().rstrip().split())
    total += (x * n)

if total == X:
    print("Yes")
else:
    print("No")