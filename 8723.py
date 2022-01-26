import sys
input = sys.stdin.readline
print = sys.stdout.write

res = list(map(int, input().strip().split()))
res.sort()
a, b, c = res
temp1 = False
temp2 = False

if c ** 2 == a ** 2 + b ** 2:
    temp1 = True
if a == b == c:
    temp2 = True

if temp1 == False and temp2 == False:
    print(str(0))
elif temp1 == True and temp2 == False:
    print(str(1))
elif temp1 == False and temp2 == True:
    print(str(2))
