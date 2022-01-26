import sys
input = sys.stdin.readline

C = int(input())

for i in range(0, C):
    temp = list(map(int, input().split()))
    tempNum = temp[0]
    total = 0
    for j in range(1, tempNum + 1):
        total += temp[j]
    average = total/tempNum
    count = 0
    for l in range(1, tempNum + 1):
        if temp[l] > average:
            count += 1
    print("{:.3f}".format(round(count/tempNum * 100, 3)) + "%")
