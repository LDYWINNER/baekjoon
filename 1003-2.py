import sys
input = sys.stdin.readline
print = sys.stdout.write

f = [[1, 0], [0, 1]]


def fibonacci(n):
    global f
    for i in range(2, n + 1):
        temp2 = [0, 0]
        temp2[0] = f[i - 1][0] + f[i - 2][0]
        temp2[1] = f[i - 1][1] + f[i - 2][1]
        f.append(temp2)


T = int(input())
for t in range(T):
    num = int(input())
    if num == 0:
        print(str(1) + " " + str(0) + "\n")
    elif num == 1:
        print(str(0) + " " + str(1) + "\n")
    else:
        fibonacci(num)
        print(str(f[-1][0]) + " " + str(f[-1][1]) + "\n")
        f = [[1, 0], [0, 1]]

