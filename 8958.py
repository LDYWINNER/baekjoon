import sys
input = sys.stdin.readline

n = int(input())

for i in range(0, n):
    quiz = str(input().split())
    temp = 1
    score = 0
    for a in quiz:
        if a == "O":
            score += temp
            temp += 1
        else:
            temp = 1
    print(score)
