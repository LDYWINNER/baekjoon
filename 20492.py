import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
print(str(N // 100 * 78) + " ")
print(str(N - (N // 100 * 20 // 100 * 22)))
