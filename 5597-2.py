import sys
input = lambda: sys.stdin.readline().rstrip()

nums = [int(input()) for _ in range(28)]

for i in range(1, 31):
    if i not in nums:
        print(i)

# 시간 좀 더 빠름 메모리는 같음
# for 문 병렬로 하나 더 돌리는게 for 문이랑 remove 같이 돌리는거보다 빠른가봄