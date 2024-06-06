import sys
input = lambda: sys.stdin.readline().rstrip()

king, queen, luke, bishop, knight, pawn = map(int, input().split())

print(1 - king, 1 - queen, 2 - luke, 2 - bishop, 2 - knight, 8 - pawn, end = " ")

