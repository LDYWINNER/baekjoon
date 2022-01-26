import sys
input = sys.stdin.readline
print = sys.stdout.write

k, w, m = map(int, input().strip().split())
print(str((w - k) // m if (w - k) % m == 0 else (w - k) // m + 1))
