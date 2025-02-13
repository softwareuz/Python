# ternary Operators 
# X if condition else Y
"""num = int(input("Enter number:"))
print("Positive" if num > 0 else "Negative")
print("EVEN" if num % 2 == 0 else "ODD")
"""
a= 4
b= 6
age = 26
temprature = 36
user_role = "admin"
max_num = a if a>b else b
min_num= a if a<b else b
status = "Adult" if age > 18 else "Child"
weather = "HOT" if temprature > 30 else "WARM"
acces = "Full Acces" if user_role == "admin" else "Limited"
print(f"Maximum number is {max_num}.")
print(f"Minimum number is {min_num}.")
print(f"Age status is {status}")
print(f"Weather is {weather}.")
print(f"Your role {acces}")
