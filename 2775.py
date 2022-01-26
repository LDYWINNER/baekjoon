import sys
input = sys.stdin.readline

T = int(input())

for i in range(0, T):
    k = int(input())
    n = int(input())

    temp = [1] * n
    for a in range(1, n):
        temp[a] = a + 1

    for j in range(0, k):
        for l in range(1, n):
            temp[l] = temp[l - 1] + temp[l]
    print(temp[n - 1])
