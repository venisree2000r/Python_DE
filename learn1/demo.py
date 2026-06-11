units = int(input("Enter your units: "))

if units <= 100:
    bill = 0
    print("No fees")

elif units <= 200:
    bill = (units - 100) * 2.25
    print("Bill Amount:", bill)
