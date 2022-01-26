d = [0] * 41


def fibo(n):
    if d[n] != 0:
        return d[n]
    if n < 2:
        return n
    else:
        d[n] = fibo(n - 1) + fibo(n - 2)
        return d[n]


T = int(input())
for i in range(T):
    n = int(input())
    if n == 0:
        print(1, 0)
    elif n == 1:
        print(0, 1)
    else:
        print(fibo(n - 1), fibo(n))

# 마지막줄 이해안감.
# 그냥 법칙인듯
