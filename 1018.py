import sys
input = sys.stdin.readline

v, h = map(int, input().split())
board = []
errorCount = []
for i in range(0, v):
    temp = str(input().rstrip())
    if i == 0:
        initialColor = temp[0]
    board.append(temp)
print("initial color", initialColor)
print("board", board)

for row in board:
    tempError = 0
    for j in range(0, h - 1):
        if row[j] == row[j + 1]:
            tempError += 1
    errorCount.append(tempError)
print(errorCount)
