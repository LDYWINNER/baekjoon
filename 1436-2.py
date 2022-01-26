N=int(input())

n=0
num=665
while(1):
    num+=1
    a=num
    while(a>=666):
        if a%1000==666:
            n+=1
            break
        a=a//10

    if n==N:
        break

print(num)