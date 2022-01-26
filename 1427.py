import sys
input = sys.stdin.readline
print = sys.stdout.write

N = str(input().rstrip())
temp = []
for n in range(len(N)):
    temp.append(int(N[n]))

temp.sort()
temp.reverse()
res = ""
for num in temp:
    res += str(num)
print(res)
