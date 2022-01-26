import sys
input = sys.stdin.readline
print = sys.stdout.write

total = 0
for i in range(4):
    total += int(input())

print(str(total // 60) + "\n")
print(str(total % 60))
