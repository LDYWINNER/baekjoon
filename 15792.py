import sys
input = sys.stdin.readline
print = sys.stdout.write

A, B = map(int, input().split())
res = str(A // B) + "."
A = (A % B) * 10

for i in range(1000):
    res += str(A // B)
    A = (A % B) * 10

print(res)