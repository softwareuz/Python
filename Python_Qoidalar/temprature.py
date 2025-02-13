user = float(input("Enter current temprature:"))
temp = input("C or F:")
if temp == "C" or temp == "c":
    F = round((user*9/5)+32 , 1)
    print(f"You choose C to F Result:{user}C = {F} F.")
elif temp == "F" or temp == "f":
    C = round((user-32)*5/9 ,1)
    print(f"You choose F to C Result: {user}F = {C}C")
else:
    print(f"{temp} is invalid value!!!")