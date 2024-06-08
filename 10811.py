import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
buckets = [str(i) for i in range(1, N + 1)]

for _ in range(M):
    i, j = map(int, input().split())
    temp = list(reversed(buckets[i-1: j]))
    buckets[i - 1: j] = temp

print(" ".join(buckets))

# 위 버전이 메모리만 좀 더 나음

# import sys
# input = lambda: sys.stdin.readline().rstrip()
#
# N, M = map(int, input().split())
# buckets = []
# for n in range(N):
#     buckets.append(str(n + 1))
#
# for _ in range(M):
#     i, j = map(int, input().split())
#     temp = list(reversed(buckets[i-1: j]))
#     for index, bucketIndex  in enumerate(list(range(i - 1, j))):
#         buckets[bucketIndex] = temp[index]
#
# print(" ".join(buckets))
