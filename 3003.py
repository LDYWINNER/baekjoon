import sys

input = sys.stdin.readline
print = sys.stdout.write

k, q, l, b, n, p = map(int, input().split())
print(str(1 - k) + " " + str(1 - q) + " " + str(2 - l) + " " + str(2 - b) + " " + str(2 - n) + " " + str(8 - p))
