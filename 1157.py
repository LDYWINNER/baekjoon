import sys
input = sys.stdin.readline

word = str(input()).rstrip().lower()
wordCount = {}
for i in range(0, len(word)):
    if word[i] not in wordCount:
        wordCount[word[i]] = 1
    else:
        wordCount[word[i]] += 1

nums = list(wordCount.values())
maxCount = max(nums)

if nums.count(maxCount) > 1:
    print("?")
else:
    for item in wordCount:
        if wordCount[item] == maxCount:
            print(item.upper())
