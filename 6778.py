import sys
input = sys.stdin.readline
print = sys.stdout.write

antenna = int(input())
eyes = int(input())

if antenna >= 3 and eyes <= 4:
    print("TroyMartian\n")
if antenna <= 6 and eyes >= 2:
    print("VladSaturnian\n")
if antenna <= 2 and eyes <= 3:
    print("GraemeMercurian\n")