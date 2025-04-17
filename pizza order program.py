print("welcome to Python's pizza")
size = input("what kind of pizza do you want S, M or L ")
bill = 0 
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill +=25
else:
    print("order not read")

pepperoni = input("Do you want extra pepperoni, type 'S' for Small and 'M' for Medium and 'L' for large ")
if pepperoni == "S":
    bill += 2
elif pepperoni == "M":
    bill += 3
elif pepperoni == "L":
    bill += 3
else: 
     print("order not read")

cheese = input("Do you want extra cheese if yes then type 'Y' and if no type 'N' ")
if cheese == "Y":
    bill += 1
else:
    print("order not read")

print(f"Your total bill will be : {bill}")