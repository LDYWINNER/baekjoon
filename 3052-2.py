import sys
input = sys.stdin.readline

nums = []
for i in range(0, 10):
    num = int(input())
    remainder = num % 42
    if remainder not in nums:
        nums.append(remainder)

print(len(nums))

# 메모리 좀 더 아낌