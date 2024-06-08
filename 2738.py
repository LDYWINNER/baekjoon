import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

res_matrix = []

for a in range(N):
    res_matrix.append(list(map(int, input().split())))

for b in range(N):
    temp = list(map(int, input().split()))
    for i in range(M):
        print(res_matrix[b][i] + temp[i], end=" ")
    print()