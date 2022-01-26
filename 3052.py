import sys
input = sys.stdin.readline

nums = []
for i in range(0, 10):
    tempNum = int(input())
    nums.append(tempNum % 42)

print(len(set(nums)))
