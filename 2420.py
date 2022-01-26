import sys
input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split())
print(str(abs(N - M)))
