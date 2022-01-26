import sys
input = sys.stdin.readline
print = sys.stdout.write

a, b, c = map(int, input().split())
temp = [a, b, c]
temp.sort()
temp = [str(x) for x in temp]
print(str(" ".join(temp)))
