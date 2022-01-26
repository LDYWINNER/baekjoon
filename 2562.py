import sys
input = sys.stdin.readline

nums = []
for j in range(0, 9):
    nums.append(int(input()))
maxNum = max(nums)

for i in range(0, len(nums)):
    if nums[i] == maxNum:
        print(nums[i])
        print(i + 1)
