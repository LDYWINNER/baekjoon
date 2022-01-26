import sys
input = sys.stdin.readline


while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break

    temp = [a, b, c]
    temp.sort()
    f = temp[0]
    s = temp[1]
    t = temp[2]

    if f + s < t:
        print("wrong")
    else:
        if f ** 2 + s ** 2 == t ** 2:
            print("right")
        else:
            print("wrong")

