import sys
input = sys.stdin.readline

N = int(input())

temp = []
n = N
temp2 = 2
if N != 1:
    while n > 1:
        if n % temp2 == 0:
            n = n // temp2
            temp.append(temp2)
        else:
            temp2 += 1

for num in temp:
    print(num)
