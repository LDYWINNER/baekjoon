import sys
input = sys.stdin.readline

N = int(input())

count = 0
temp = list(map(int, input().split()))
for num in temp:
    if num == 1:
        continue
    elif num == 2:
        count += 1
    else:
        count += 1
        for i in range(2, num):
            if num % i == 0:
                count -= 1
                break
print(count)
