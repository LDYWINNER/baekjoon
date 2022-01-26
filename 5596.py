import sys
input = sys.stdin.readline
print = sys.stdout.write

total1, total2 = 0, 0
temp1 = list(map(int, input().split()))
temp2 = list(map(int, input().split()))

for i in range(4):
    total1 += temp1[i]
    total2 += temp2[i]

if total1 == total2:
    print(str(total1))
else:
    print(str(max([total1, total2])))
