import sys
input = sys.stdin.readline
A, B = map(int, input().split())
while A != 0 or B != 0:
    print(A + B)
    A, B = map(int, input().split())

# 10952 원본은 틀림. 0 0 만 제외시키는건 이 코드임.