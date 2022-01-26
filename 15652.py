import sys
from itertools import product

input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split())
temp = [str(x) for x in range(1, N + 1)]
if M == 1:
    for num in temp:
        print(str(num) + "\n")


else:
    for num in product(temp, repeat=M):
        temp3 = True
        for i in range(0, M - 1):
            if int(num[i]) > int(num[i + 1]):
                temp3 = False
        if temp3:
            temp2 = list(num)
            print(" ".join(temp2) + "\n")
