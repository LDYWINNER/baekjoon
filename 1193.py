import sys
input = sys.stdin.readline

x = int(input())

numMade = 5
temp = 4
while True:
    if x == 1:
        print("1/1")
        break

    if x < numMade:
        numSum = temp // 4 + 1

    else:
        numMade += temp
        temp += 4
