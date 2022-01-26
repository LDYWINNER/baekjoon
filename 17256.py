import sys
input = sys.stdin.readline
print = sys.stdout.write

ax, ay, az = map(int, input().split())
cx, cy, cz = map(int, input().split())

bx = cx - az
by = round(cy / ay)
bz = cz - ax
print(str(bx) + " " + str(by) + " " + str(bz))
