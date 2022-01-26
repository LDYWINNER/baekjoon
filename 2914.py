import sys
input = sys.stdin.readline
print = sys.stdout.write

A, I = map(int, input().split())
print(str(A * (I - 1) + 1))
