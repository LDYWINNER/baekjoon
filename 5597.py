import sys
input = lambda: sys.stdin.readline().rstrip()

nums = list(range(1, 31))

for _ in range(28):
    submit = int(input())
    nums.remove(submit)

print(nums[0])
print(nums[1])
