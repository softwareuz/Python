user = float(input("Enter your weight:"))
typ = input("Kg or Lbs (K or L):")
if typ == "K" or typ == "k":
    lbs = user * 2.204
    print(f"You chose kgs to lbs and the result is {user} kgs = {round(lbs, 2)} lbs")
elif typ == "L" or typ == "l":
    kgs = user / 2.204
    print(f"You chose lbs to kgs and the result is {user} lbs = {round(kgs, 2)} kgs")
else:
    print(f"{typ} is not a valid value!!")
