import sys
input = sys.stdin.readline
print = sys.stdout.write
# DP
reference = {}


def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if a < b < c:
        if (a, b, c) in reference:
            return reference[(a, b, c)]
        else:
            temp = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
            reference[(a, b, c)] = temp
            return temp
    else:
        if (a, b, c) in reference:
            return reference[(a, b, c)]
        else:
            temp = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
            reference[(a, b, c)] = temp
            return temp


while True:
    ia, ib, ic = map(int, input().split())

    if ia == -1 and ib == -1 and ic == -1:
        break

    print("w(" + str(ia) + ", " + str(ib) + ", " + str(ic) + ") = " + str(w(ia, ib, ic)) + '\n')
