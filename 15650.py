import sys
from itertools import permutations

input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split())
temp = [str(x) for x in range(1, N + 1)]
# print(str(temp))
if M == 1:
    for num in temp:
        print(str(num) + "\n")
else:
    combs = list(permutations(temp, M))
    for com in combs:
        temp3 = True
        for i in range(0, M - 1):
            if int(com[i]) > int(com[i + 1]):
                temp3 = False
        if temp3:
            temp2 = list(com)
            print(" ".join(temp2) + "\n")
