import sys
input = sys.stdin.readline
print = sys.stdout.write

A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
scores = [A, B, C, D, E]
total = 0
for score in scores:
    if score < 40:
        total += 40
    else:
        total += score

print(str(round(total / 5)))
