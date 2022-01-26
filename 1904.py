import sys
import math
input = sys.stdin.readline
print = sys.stdout.write

# 정직한 풀이 ㅋㅋ
def helper(n):
    result = 0
    temp = n // 2
    if (n // 2) * 2 == n:
        temp -= 1
    for i in range(1, temp + 1):
        temp1 = i + n - (i * 2)
        res1 = math.factorial(temp1)
        if i == 1:
            temp2 = n - (i * 2)
            res2 = math.factorial(temp2)
            #print(str(res1 // res2) + '\n')
            result += (res1 // res2)
        else:
            temp2 = n - (i * 2)
            res2 = math.factorial(temp2)
            res3 = math.factorial(i)
            #print(str(res1 // res2 // res3) + '\n')
            result += (res1 // res2 // res3)
    #print(str(result) + "\n")
    return result


def count_sequence(n):
    total = 1 # all one
    if n % 2 == 0:
        total += 1
    if n == 3:
        total += 2 # 001, 100
    if n > 3:
        total += helper(n)
    return total


N = int(input())
print(str(count_sequence(N) % 15746))
