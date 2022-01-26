import sys
input = sys.stdin.readline

word = str(input().rstrip())
timeCount = 0
for i in range(0, len(word)):
    if word[i] in ['A', 'B', 'C']:
        timeCount += 3
    elif word[i] in ['D', 'E', 'F']:
        timeCount += 4
    elif word[i] in ['G', 'H', 'I']:
        timeCount += 5
    elif word[i] in ['J', 'K', 'L']:
        timeCount += 6
    elif word[i] in ['M', 'N', 'O']:
        timeCount += 7
    elif word[i] in ['P', 'Q', 'R', 'S']:
        timeCount += 8
    elif word[i] in ['T', 'U', 'V']:
        timeCount += 9
    elif word[i] in ['W', 'X', 'Y', 'Z']:
        timeCount += 10
    else:
        timeCount += 11
print(timeCount)
