import sys
input = sys.stdin.readline

T = input()

for i in range(int(T)):
    row = input().rstrip()
    print(row[0] + row[-1])
