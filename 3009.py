import sys
input = sys.stdin.readline

pairs = []
for i in range(0, 3):
    x, y = map(int, input().split())
    pairs.append([x, y])

# 1. common x finding
x = []
y = []
for pair in pairs:
    x.append(pair[0])
    y.append(pair[1])

x.sort()
x1 = x[0]
x2 = x[2]
y.sort()
y1 = y[0]
y2 = y[2]
if x.count(x1) == 2 and y.count(y1) == 1:
    print(x2, y1)
elif x.count(x1) == 2 and y.count(y1) == 2:
    print(x2, y2)
elif x.count(x1) == 1 and y.count(y1) == 1:
    print(x1, y1)
else:
    print(x1, y2)

