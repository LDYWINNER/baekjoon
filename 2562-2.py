import sys
input = sys.stdin.readline

nums = []
for j in range(0, 9):
    nums.append(int(input()))
maxNum = max(nums)

index = nums.index(maxNum)

print(maxNum)
print(index + 1)

# for문에서 index 내장 함수로 바꿨는데 메모리는 확실히 줄었고 시간은 아주 조금 늘었음