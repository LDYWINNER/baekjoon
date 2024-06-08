import sys
input = sys.stdin.readline

nums = set()

for i in range(10):
    num = int(input())
    nums.add(num % 42)

print(len(nums))

# 비슷함 최적화 두번째 버전이랑