import sys
input = sys.stdin.readline
print = sys.stdout.write

limit = int(input())
current_speed = int(input())
dif = current_speed - limit

if dif <= 0:
    print("Congratulations, you are within the speed limit!")
elif 1 <= dif <= 20:
    print("You are speeding and your fine is $100.")
elif 21 <= dif <= 30:
    print("You are speeding and your fine is $270.")
elif dif >= 31:
    print("You are speeding and your fine is $500.")
