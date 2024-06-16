import sys
input = lambda: sys.stdin.readline().rstrip()

num_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

N, B = map(int, input().split())
total = ""

while N:
    total += num_list[N % B]
    N //= B

print(total[::-1])