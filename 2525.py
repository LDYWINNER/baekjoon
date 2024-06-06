import sys
input = sys.stdin.readline
print = sys.stdout.write

H, M = map(int, input().split())
timer = int(input())
hour = H + timer // 60
minute = M + timer % 60

while minute >= 60:
    hour += 1
    minute -= 60

while hour >= 24:
    hour -= 24

print(str(hour) + " " + str(minute))
