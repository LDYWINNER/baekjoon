import sys
input = sys.stdin.readline
print = sys.stdout.write

n1, k1, n2, k2 = map(int, input().split())
print(str(n1 * k1 + n2 * k2))
