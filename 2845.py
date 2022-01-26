import sys

input = sys.stdin.readline
print = sys.stdout.write

L, P = map(int, input().split())
answer = L * P
a, b, c, d, e = map(int, input().split())
print(str(a - answer) + " " + str(b - answer) + " " + str(c - answer) + " " + str(d - answer) + " " + str(e - answer))
