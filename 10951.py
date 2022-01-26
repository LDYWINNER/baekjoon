import sys
input = sys.stdin.readline

try:
    while True:
        A, B = map(int, input().split())
        print(A + B)
except:
    print("")