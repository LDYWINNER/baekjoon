import sys
input = sys.stdin.readline
print = sys.stdout.write

A, B = map(int, input().split())
C = int(input())
temp1 = C // 60
temp2 = C % 60
hour = A + temp1
minute = B + temp2

while minute >= 60:
    hour += 1
    minute -= 60

while hour >= 24:
    hour -= 24

print(str(hour) + " " + str(minute))
