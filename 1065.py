import sys
input = sys.stdin.readline

n = int(input())

count = 0
for num in range(1, n + 1):
    if 1 <= num <= 99:
        count += 1
    else:
        f = num // 100
        s = num // 10 % 10
        t = num % 10
        if (f - s) == (s - t):
            count += 1
print(count)
