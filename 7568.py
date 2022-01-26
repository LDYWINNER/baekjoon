import sys
input = sys.stdin.readline

N = int(input())
people = []
for n in range(0, N):
    x, y = map(int, input().split())
    people.append([x, y])

res = []
for i in range(0, len(people)):
    temp = people.pop(0)
    count = 0
    for person in people:
        if person[0] > temp[0] and person[1] > temp[1]:
            count += 1
    people.append(temp)
    res.append(count + 1)

for r in res:
    print(r, end=" ")
