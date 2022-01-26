import sys
import math
input = sys.stdin.readline
print = sys.stdout.write

n1, n2, n12 = map(int, input().split())
print(str(math.floor((n1 + 1) * (n2 + 1) / (n12 + 1) - 1)))
