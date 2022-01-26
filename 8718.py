import sys
input = sys.stdin.readline
print = sys.stdout.write

x, k = map(int, input().strip().split())
if x >= 7 * k:
    print(str(int(7 * k * 1000)))
elif x >= 3.5 * k:
    print(str(int(3.5 * k * 1000)))
elif x >= 1.75 * k:
    print(str(int(1.75 * k * 1000)))
else:
    print(str(0))
