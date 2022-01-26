import sys
input = sys.stdin.readline
print = sys.stdout.write

temp = str(input())
temp2 = int(temp, 2)
res1 = 17 * temp2
print(str(bin(res1))[2:])
