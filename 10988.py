import sys
input = lambda: sys.stdin.readline().rstrip()

word = input()

if word == word[::-1]:
    print(1)
else:
    print(0)