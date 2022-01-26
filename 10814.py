import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
people = {}
for n in range(N):
    age, name = map(str, input().split())
    if int(age) in people:
        people[int(age)].append(name)
    else:
        people[int(age)] = [name]
temp = sorted(people)
for ageNum in temp:
    for person in people[ageNum]:
        print(str(ageNum) + " " + person + "\n")
