import sys
input = sys.stdin.readline
print = sys.stdout.write

K, D, A = map(int, input().split("/"))
if K + A < D or D == 0:
    print("hasu")
else:
    print("gosu")
