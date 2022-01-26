import sys
input = sys.stdin.readline
print = sys.stdout.write

n, m = map(int, input().split())
print(str(n // m) + "\n")
print(str(n % m))
