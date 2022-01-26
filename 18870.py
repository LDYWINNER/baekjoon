# 시간 초과뜸
# time complexity: dict better than list
# 18870-2.py dict 풀이
import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
nums = list(map(int, input().split()))
#print(str(nums))

temp = list(set(nums))
temp = sorted(temp, reverse=False)

#print(str(temp))
res = [0]
for i in range(1, len(temp)):
    count = 0
    for j in range(0, i):
        if temp[j] < temp[i]:
            count += 1
    res.append(count)
#print(str(res))

for num in nums:
    print(str(res[temp.index(num)]) + " ")
