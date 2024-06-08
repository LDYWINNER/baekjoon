import sys
input = lambda: sys.stdin.readline().rstrip()

temp = ""

for _ in range(5):
    row = input()
    temp += row
    if len(row) < 15:
        temp += " " * (15 - len(row))

for j in range(15):
    for k in range(5):
        if temp[15 * k + j] != " ":
            print(temp[15 * k + j], end="")
