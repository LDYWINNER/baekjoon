import sys
input = sys.stdin.readline

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
time = 0
for j in range(len(a)):
    for i in dial:
        if a[j] in i:
            time += dial.index(i) + 3
print(time)

# if문으로 케이스 분류하는게 시간은 덜 걸림
# 이건 메모리 덜 쓰고 코드 짧은 버전