import sys
input = sys.stdin.readline

str_nums = input().split()
sang_soo_nums = []

for num in str_nums:
    sang_soo_nums.append(num[::-1])

real_nums = map(int, sang_soo_nums)

print(max(real_nums))

# 문자열 슬라이싱 사용하여 최적화한 버전