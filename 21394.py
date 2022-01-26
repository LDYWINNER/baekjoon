import sys

input = sys.stdin.readline

T = int(input())

for t in range(0, T):
    numCount = list(map(int, input().split()))
    nums = []
    res = []
    temp = 1
    for n in numCount:
        if numCount[5] > 0:
            numCount[-1] += numCount[5]
            numCount[5] = 0
        if n == 0:
            temp += 1
            continue
        else:
            for i in range(0, n):
                nums.append(temp)
            temp += 1

    temp2 = True
    lenNums = len(nums)
    if lenNums % 2 == 1:
        res.append(nums[0])
        for i in range(1, lenNums):
            if temp2 is True:
                res.append(nums[i])
                temp2 = False
            else:
                res.insert(0, nums[i])
                temp2 = True
    else:
        res.append(nums[0])
        for i in range(1, lenNums):
            if temp2 is True:
                res.insert(0, nums[i])
                temp2 = False
            else:
                res.append(nums[i])
                temp2 = True

    for r in res:
        print(r, end=" ")
