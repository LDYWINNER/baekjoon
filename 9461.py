import sys
input = sys.stdin.readline
print = sys.stdout.write

res = [0] * 101
res[1], res[2], res[3] = 1, 1, 1
res[4], res[5] = 2, 2
res[6] = 3
T = int(input())
for t in range(T):
    N = int(input())
    if N <= 6:
        print(str(res[N]) + '\n')
    else:
        for i in range(7, N + 1):
            res[i] = res[i - 1] + res[i - 5]
        print(str(res[N]) + '\n')
