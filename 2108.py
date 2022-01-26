import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
nums = []
total = 0
for n in range(N):
    temp = int(input())
    total += temp
    nums.append(temp)
nums.sort()

count_nums = {}
for num in nums:
    if num not in count_nums:
        count_nums[num] = 1
    else:
        count_nums[num] += 1
#print(str(count_nums) + "\n")

value = list(count_nums.values())
value.sort()
max_num = max(value)
res = []
for key in count_nums:
    if count_nums[key] == max_num:
        res.append(key)


print(str(round(total / N)) + "\n")
print(str(nums[N // 2]) + "\n")
if len(res) > 1:
    print(str(res[1]) + "\n")
else:
    print(str(res[0]) + "\n")
print(str(nums[-1] - nums[0]) + "\n")


