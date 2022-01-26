import sys
input = sys.stdin.readline
print = sys.stdout.write

res = 2
dif = 2
N = int(input())
if N == 1:
    print(str(2))
else:
    if N % 2 == 0:
        print(str((N // 2 + 1) ** 2))
    else:
        temp = ((N + 1) // 2 + 1) ** 2
        print(str(temp - ((N + 1) // 2 + 1)))

