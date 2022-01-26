import sys
input = sys.stdin.readline
print = sys.stdout.write

A, B, C = map(int, input().split())
D = int(input())
temp1 = D // 3600
temp2 = (D % 3600) // 60
temp3 = (D % 3600) % 60
hour = A + temp1
minute = B + temp2
second = C + temp3

while second >= 60:
    minute += 1
    second -= 60

while minute >= 60:
    hour += 1
    minute -= 60

while hour >= 24:
    hour -= 24

print(str(hour) + " " + str(minute) + " " + str(second))
