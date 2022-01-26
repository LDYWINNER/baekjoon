import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
for x in range(n):
    temp = list(map(int, input().split()))
    print(str(temp))

