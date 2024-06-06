import sys
input = sys.stdin.readline

T = int(input().rstrip())

try:
    for i in range(T):
        A, B = map(int, input().split(","))
        print(A + B)
except:
    print("")
