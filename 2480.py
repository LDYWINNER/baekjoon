import sys
input = sys.stdin.readline
print = sys.stdout.write

nums = list(map(int, input().split()))
if nums[0] == nums[1] == nums[2]:
    print(str(10000 + (1000 * nums[0])))
elif (nums[0] != nums[1]) and (nums[1] != nums[2]) and (nums[0] != nums[2]):
    print(str(max(nums) * 100))
else:
    for num in nums:
        if nums.count(num) == 2:
            print(str(1000 + (100 * num)))
            break
