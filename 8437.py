import sys
input = sys.stdin.readline
print = sys.stdout.write

total = int(input())
dif = int(input())
temp = (total - dif) // 2
print(str(temp + dif) + "\n")
print(str(temp))
