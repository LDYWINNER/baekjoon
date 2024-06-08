import sys
input = lambda: sys.stdin.readline().rstrip()

max_num = -sys.maxsize
res_row = 0
res_column = 0

for i in range(9):
    row = list(map(int, input().split()))
    for j in range(9):
        if row[j] > max_num:
            max_num = row[j]
            res_row = i + 1
            res_column = j + 1

print(max_num)
print(res_row, res_column)