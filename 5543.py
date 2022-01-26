import sys
input = sys.stdin.readline
print = sys.stdout.write

sb = int(input())
jb = int(input())
hb = int(input())
coke = int(input())
cidar = int(input())
print(str(min([sb, jb, hb]) + min([coke, cidar]) - 50))
