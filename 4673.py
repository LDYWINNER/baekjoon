res = list(range(1, 10001))
ref = res

for num in ref:
    while True:
        if num < 10:
            num = num + num
        elif num < 100:
            num = num + (num // 10) + (num % 10)
        elif num < 1000:
            num = num + (num // 100) + (num // 10 % 10) + (num % 10)
        else:
            num = num + (num // 1000) + (num // 100 % 10) + (num // 10 % 10) + (num % 10)

        if num > 10000:
            break

        if num not in res:
            continue
        res.remove(num)

for r in res:
    print(r)
