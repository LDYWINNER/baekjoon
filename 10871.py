import sys

input = sys.stdin.readline
N, X = map(int, input().split())
nums = input().split()
for i in range(0, N):
    if int(nums[i]) < X:
        print(nums[i], end=" ")
