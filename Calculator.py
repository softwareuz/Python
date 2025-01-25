#6-kun Python Calculator

operator = (input("Choose a operator(+,-,*,/):"))
num1 = float(input("Enter 1st number:"))
num2 = float(input("Enter 2nd number:"))
if operator == "+":
    result = num1+num2
    print(f"The sum of {num1} and {num2} is :{result}")
elif operator == "-":
    result = num1-num2
    print(f"The Sub of {num1} and {num2} is :{result}")
elif operator == "*":
    result = num1*num2
    print(f"The mul is {num1} and {num2} is: {result}")
elif operator == "/":
    result = num1/num2
    print(f"The div of {num1} and {num2} is: {result}")
else:
    print(f"{operator} is invalid choice for this program!!!")
