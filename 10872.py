import sys
input = sys.stdin.readline

N = int(input())

if N == 0 or N == 1:
    print(1)
else:
    result = 1
    temp = N
    while temp != 1:
        result *= temp
        temp -= 1
    print(result)
