import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
ref = [0] * 1000001
ref[0] = 1
ref[1] = 2
for i in range(2, N):
    ref[i] = (ref[i - 1] + ref[i - 2]) % 15746

print(str(ref[N - 1]))
