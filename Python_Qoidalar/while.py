#while loop = excute some code conditions remain true

name = input("Enter your name: ")
while name == "":
    print("You did not enter your name!!!")
    name = input("Enter your name: ")
print(f"Hello {name}")

age = int(input("Enter your age:"))
while age < 0:
    print("Age can't be negative")
    age = int(input("Enter your age:"))
print(f"You are {age} years old")

food = input("Enter a food you like (q for exit):")
while not food == "q" or food == "Q":
    print(f"You like food {food}")
    food = input("Enter another food you like (q for exit):")
print("Good bye see you!!!")

num = int(input("Enter one number # 1-10:"))
while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter again one number between 1-10:"))
print(f"Yourt number is {num}")
