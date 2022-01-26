import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
words = {}
for n in range(N):
    temp = str(input().rstrip())
    if len(temp) in words:
        words[len(temp)].append(temp)
    else:
        words[len(temp)] = [temp]
#print(str(words))
temp = sorted(words)
for length in temp:
    temp2 = list(set(words[length]))
    temp2.sort()
    for word in temp2:
        print(word + "\n")

