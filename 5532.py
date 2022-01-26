import sys
input = sys.stdin.readline
print = sys.stdout.write

L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

temp = max([A // C, B // D])
if (A // C) > (B // D):
    if A % C == 0:
        temp = A // C
    else:
        temp = A // C + 1
else:
    if B % D == 0:
        temp = B // D
    else:
        temp = B // D + 1

print(str(L - temp))
