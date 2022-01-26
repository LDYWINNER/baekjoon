import sys
input = sys.stdin.readline

word = str(input().rstrip())
reference = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
temp = ''
wordCount = 0
tempNum = 0
while True:
    if (("c" not in word) and ("=" not in word) and ("-" not in word) and ("d" not in word) and ("z" not in word) and \
            ("l" not in word) and ("j" not in word) and ("n" not in word) and ("s" not in word)) or (len(word) - tempNum < 2):
        break
    if word[tempNum:tempNum + 2] in reference:
        wordCount += 1
        word = word[:tempNum] + word[tempNum + 2:]
    elif word[tempNum:tempNum + 3] in reference:
        wordCount += 1
        word = word[:tempNum] + word[tempNum + 3:]
    else:
        tempNum += 1
wordCount += len(word)
print(wordCount)
