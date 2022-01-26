import sys
input = sys.stdin.readline
print = sys.stdout.write

N, M, K = map(int, input().split())
if (K + 1) % M != 0:
    temp = (K + 1) // M
else:
    temp = (K + 1) // M - 1
temp2 = (K + 1) % M
if temp2 > 0:
    print(str(temp) + " " + str(temp2 - 1))
else:
    print(str(temp) + " " + str(M - 1))
