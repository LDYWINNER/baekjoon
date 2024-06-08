import sys
input = lambda: sys.stdin.readline().rstrip()

N = input()

numbers = list(map(int, input().split()))

v = int(input())

print(numbers.count(v))