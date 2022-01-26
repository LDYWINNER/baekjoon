import sys
import math
input = sys.stdin.readline

r = int(input())
print(math.pi * r ** 2)

side = math.sqrt(r ** 2 * 2)
print(side ** 2)