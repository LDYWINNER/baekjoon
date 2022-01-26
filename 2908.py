import sys
input = sys.stdin.readline

two_nums = list(map(int, input().split()))
new_nums = []
for num in two_nums:
    newNum = (num % 10 * 100) + (num // 10 % 10 * 10) + (num // 100)
    new_nums.append(newNum)

print(max(new_nums))

