import sys
input = sys.stdin.readline
print = sys.stdout.write

first = int(input())
second = int(input())
third = int(input())

total = 91
print("The 1-3-sum is " + str(total + first + second * 3 + third))
