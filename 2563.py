import sys
input = lambda: sys.stdin.readline().rstrip()

paper = [[0 for _ in range(100)] for _ in range(100)]
count = 0

N = int(input())

for i in range(N):
    left, bottom = map(int, input().split())

    for x in range(left, left + 10):
        for y in range(bottom, bottom + 10):
            paper[x][y] = 1

for row in paper:
    count += row.count(1)

print(count)