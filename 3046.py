import sys
input = sys.stdin.readline
print = sys.stdout.write

R1, S = map(int, input().split())
print(str(S * 2 - R1))
