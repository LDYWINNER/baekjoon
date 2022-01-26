import sys
input = sys.stdin.readline

N = int(input())

if N == 1:
    print(1)
else:
    temp = 1
    sumWhat = 6
    rooms = 1
    while temp < N:
        temp += sumWhat
        sumWhat += 6
        rooms += 1
    print(rooms)
