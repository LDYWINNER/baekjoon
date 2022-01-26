import sys
input = sys.stdin.readline
print = sys.stdout.write

S, K, H = map(int, input().split())
if S + K + H >= 100:
    print("OK")
else:
    temp = min([S, K, H])
    if temp == S:
        print("Soongsil")
    elif temp == K:
        print("Korea")
    elif temp == H:
        print("Hanyang")
