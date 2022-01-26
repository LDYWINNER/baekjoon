import sys
input = sys.stdin.readline

x, y, w, h = map(int, input().split())

temp1 = h - y
temp2 = w - x

print(min(temp1, temp2, x, y))
