import sys
# bubble sort
input = sys.stdin.readline
write = sys.stdout.write

N = int(input())
nums = [int(input()) for n in range(N)]


def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        swapped = False
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


bubble_sort(nums)
for num in nums:
    print(num)
