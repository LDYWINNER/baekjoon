import sys
input = sys.stdin.readline
print = sys.stdout.write

temp = []
for i in range(2):
    temp.append(int(input()))

print(str(temp[0] + temp[1]) + "\n")
print(str(temp[0] - temp[1]) + "\n")
print(str(temp[0] * temp[1]) + "\n")
