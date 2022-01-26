import sys
input = sys.stdin.readline
write = sys.stdout.write

N = int(input())
nums = [int(input()) for n in range(N)]
nums.sort()
for num in nums:
    print(num)
