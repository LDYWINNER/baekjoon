import sys
input = sys.stdin.readline
print = sys.stdout.write

total = 0
for i in range(5):
    temp = int(input())
    total += temp

print(str(total))
