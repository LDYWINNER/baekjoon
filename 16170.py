from datetime import datetime

today = datetime.utcnow().strftime("%Y-%m-%d")
temp = today.split("-")
for t in temp:
    print(t)
