import sys
from itertools import permutations
input = sys.stdin.readline
print = sys.stdout.write

temp = [0, 1, 2]
prices = []
tempRes = 0
N = int(input())
indexes = list(permutations(temp, N))
for n in range(N):
    Rcost, Gcost, Bcost = map(int, input().split())
    prices.append([Rcost, Gcost, Bcost])

#for index in indexes:
 #   temp2 =
