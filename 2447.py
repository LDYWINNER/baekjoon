def star(n):
    if n == 3:
        star_list = ['***', '* *', '***']
        return star_list
    else:
        new_star_list = [x * 3 for x in star(n//3)] + [x + ' '*(n//3) + x for x in star(n//3)] + [x * 3 for x in star(n//3)]
        return new_star_list


for i in star(int(input())):
    print(i)
