import collections
import sys
input = sys.stdin.readline
print = sys.stdout.write

nums = list(map(int, input().split()))
counts = collections.Counter(nums)

if len(counts) == 1:
    print(str(10000 + (1000 * nums[0])))
elif len(counts) == 2:
    print(str(1000 + (100 * counts.most_common(1)[0][0])))
else:
    print(str(max(nums) * 100))

# 오히려 메모리랑 시간 더 들었음