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

# H, M = map(int, input().split())
#
# if M < 45:  # 분단위가 45분보다 작을 때
#     if H == 0:  # 0 시이면
#         H = 23
#         M += 60
#     else:  # 0시가 아니면 (0시보다 크면)
#         H -= 1
#         M += 60
#
# print(H, M - 45)
