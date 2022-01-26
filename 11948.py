import sys
input = sys.stdin.readline
print = sys.stdout.write

A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
F = int(input())

temp1 = max([A + B + C, A + B + D, B + C + D, A + C + D])
temp2 = max([E, F])
print(str(temp1 + temp2))
