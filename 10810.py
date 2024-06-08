import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
buckets = ["0"] * N

for _ in range(M):
    i, j, k = map(int, input().split())
    for index in range(i - 1, j):
        buckets[index] = str(k)

print(" ".join(buckets))
