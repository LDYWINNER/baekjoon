import sys
input = sys.stdin.readline
print = sys.stdout.write

a, b, c, d, e = map(int, input().split())

temp = (a ** 2) + (b ** 2) + (c ** 2) + (d ** 2) + (e ** 2)
print(str(temp % 10))
