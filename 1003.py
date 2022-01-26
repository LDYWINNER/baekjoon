import sys
input = sys.stdin.readline
print = sys.stdout.write
# 시간초과 (not dp)
temp = [0, 0]
def fibonacci(n):
    global temp
    if n == 0:
        temp[0] += 1
        return 0
    elif n == 1:
        temp[1] += 1
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


T = int(input())
for t in range(T):
    num = int(input())
    fibonacci(num)
    print(str(temp))
    temp = [0, 0]

