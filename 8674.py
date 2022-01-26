import sys
input = sys.stdin.readline
print = sys.stdout.write

a, b = map(int, input().split())
if a % 2 == 0 or b % 2 == 0:
    print(str(0))
else:
    print(str(min([a, b])))
