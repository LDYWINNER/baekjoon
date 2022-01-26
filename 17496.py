import sys
input = sys.stdin.readline
print = sys.stdout.write

N, T, C, P = map(int, input().split())
temp = N - T - 1
dates = temp // T + 1
count = dates * C
print(str(count * P))
