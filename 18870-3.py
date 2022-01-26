import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
nums = list(map(int, input().split()))
#print(str(nums))

temp = list(set(nums))
temp = sorted(temp, reverse=False)

#print(str(temp))
for num in nums:
    print(str(temp.index(num)) + " ")
