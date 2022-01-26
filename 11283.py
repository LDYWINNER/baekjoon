import sys
input = sys.stdin.readline
print = sys.stdout.write

# ord(): str 을 받아서 유니코드 번호로 반환
temp = str(input().rstrip())
print(str(ord(temp) - 44031))
