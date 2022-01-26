from datetime import datetime

today = datetime.today()
temp = str(today)
temp2 = int(temp[11:13]) + 9
if temp2 > 24:
    temp3 = int(temp[8:10])
    temp3 += 1
    if temp3 < 10:
        temp3 = "0" + str(temp3)
    print(temp[:8] + str(temp3))
else:
    print(temp[:10])
