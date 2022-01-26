# dict 풀이
# 18870-3.py : 18870 1차 최적화
import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
nums = list(map(int, input().split()))
#print(str(nums))

temp = list(set(nums))
temp = sorted(temp, reverse=False)

#print(str(temp))
res = {}
for t in range(len(temp)):
    res[temp[t]] = t

for num in nums:
    print(str(res[num]) + " ")
