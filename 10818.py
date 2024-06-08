import sys
input = sys.stdin.readline

_ = input()
nums = list(map(int, input().split()))
nums.sort()

print(nums[0], nums[-1])
