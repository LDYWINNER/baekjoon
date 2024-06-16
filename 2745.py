import sys
input = lambda: sys.stdin.readline().rstrip()

num_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

N, B = input().split()
total = 0
for i, num in enumerate(N[::-1]):
    total += int(B) ** i * num_list.index(num)

print(total)