import sys
input = sys.stdin.readline

N = int(input())

for i in range(1, N):
    length = len(str(i))
    stringNum = str(i)
    tempNum = i
    for j in range(0, length):
        #print("stringNum", stringNum)
        tempNum += int(stringNum[-1])
        stringNum = stringNum[:-1]
    #print("tempNum", tempNum)
    if tempNum == N:
        print(i)
        break
else:
    print(0)
