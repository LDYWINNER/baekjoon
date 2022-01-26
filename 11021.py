import sys

input = sys.stdin.readline
T = int(input())
for i in range(0, T):
    A, B = map(int, input().split())
    print("Case #" + str(i + 1) + ":", A + B)
