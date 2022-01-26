import sys
input = sys.stdin.readline


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

M, N = map(int, input().split())
temp = sieve(N)
for num in temp:
    if num >= M:
        print(num)
