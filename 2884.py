H, M = map(int, input().split())
M = M - 45
if M < 0 and H == 0:
    print(H + 23, M + 60)
elif H == 0:
    print(0, M)
elif M < 0:
    print(H - 1, M + 60)
else:
    print(H, M)
