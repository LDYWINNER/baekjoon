import sys
from math import ceil
input = sys.stdin.readline

A, B, V = map(int, input().split())

if A > V:
    print(1)
else:
    print(ceil((V - A) / (A - B)) + 1)
