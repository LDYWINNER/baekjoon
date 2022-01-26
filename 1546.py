import sys
input = sys.stdin.readline

N = int(input())

temp = 0
nums = list(map(int, input().split()))
maxNum = max(nums)
for num in nums:
    temp += (num / maxNum * 100)

print(temp / N)
