import sys
input = lambda: sys.stdin.readline().rstrip()

grade_list = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0,
}

total_grade = 0
total_credit = 0
for i in range(20):
    _, credit, grade = input().split()
    if grade != "P":
        total_grade += (float(credit) * grade_list[grade])
        total_credit += float(credit)

result = str(int(total_grade // total_credit)) + "."
total_grade = (total_grade % total_credit) * 10
for j in range(5):
    result += str(int(total_grade // total_credit))
    total_grade = (total_grade % total_credit) * 10

print(result)