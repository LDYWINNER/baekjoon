import sys
input = sys.stdin.readline

_ = input()
nums = list(map(int, input().split()))

print(min(nums), max(nums))

# min max 내장 함수 이용하는게 sort해서 구하는거보다 훨씬 빠름