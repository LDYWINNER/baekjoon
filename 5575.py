import sys
input = sys.stdin.readline
print = sys.stdout.write

res = []
for i in range(3):
    h1, m1, s1, h2, m2, s2 = map(int, input().split())
    tempH = h2 - h1
    tempM = m2 - m1
    tempS = s2 - s1

    if tempS < 0:
        if tempM == 0:
            tempH -= 1
            tempM = 59
            tempS = 60 + tempS
            res.append(tempH)
            res.append(tempM)
            res.append(tempS)
        elif tempM < 0:
            tempH -= 1
            tempM = 59 + tempM
            tempS = 60 + tempS
            res.append(tempH)
            res.append(tempM)
            res.append(tempS)
        else:
            tempM -= 1
            tempS = 60 + tempS
            res.append(tempH)
            res.append(tempM)
            res.append(tempS)
    elif tempM < 0 and tempS >= 0:
        tempH -= 1
        tempM = 60 + tempM
        res.append(tempH)
        res.append(tempM)
        res.append(tempS)
    else:
        res.append(tempH)
        res.append(tempM)
        res.append(tempS)
#print(str(res))
for j in range(0, len(res), 3):
    print(str(res[j]) + " " + str(res[j + 1]) + " " + str(res[j + 2]) + "\n")