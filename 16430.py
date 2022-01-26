import sys
input = sys.stdin.readline
print = sys.stdout.write

A, B = map(int, input().split())
print(str(B - A) + " " + str(B))
