import sys
import math
input = sys.stdin.readline
print = sys.stdout.write

D, H, W = map(int, input().split())
temp = (1 + (W ** 2 / H ** 2))
x = (D ** 2 / temp) ** (1/2)
y = x * W / H
print(str(math.floor(x)) + " " + str(math.floor(y)))
