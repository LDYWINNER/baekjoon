import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
temp = {}
for n in range(N):
    x, y = map(int, input().split())
    if y in temp:
        temp[y].append(x)
    else:
        temp[y] = [x]
#print(str(temp))
temp2 = sorted(temp)
for key in temp2:
    temp[key].sort()
    for value in temp[key]:
        print(str(value) + " " + str(key) + "\n")
