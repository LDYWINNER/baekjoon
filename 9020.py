import sys
input = sys.stdin.readline

T = int(input())


def sieve(n):
    e = [True for _ in range(n + 1)]
    e[0], e[1] = False, False
    primes = list()
    for i in range(2, n + 1):
        if e[i]:
            primes.append(i)
            for j in range(i * 2, n + 1, i):
                e[j] = False
    return primes


for t in range(0, T):
    n = int(input())
    r = sieve(n)
    temp = []
    for num in r:
        if num * 2 == n:
            print(num, num)
            break
        if (n - num) in r:
            temp.append(num)
    else:
        if len(temp) == 2:
            print(temp[0], temp[1])
        else:
            l = len(temp)
            print(temp[l // 2 - 1], temp[l // 2])

