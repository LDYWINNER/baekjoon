import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
buckets = []
for n in range(N):
    buckets.append(str(n + 1))

for _ in range(M):
    i, j = map(int, input().split())
    temp = buckets[i - 1]
    buckets[i - 1] = buckets[j - 1]
    buckets[j - 1] = temp

print(" ".join(buckets))
