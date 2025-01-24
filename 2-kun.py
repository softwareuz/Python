#2-kun
#Typecasting
ism = "Ahrorjon"
yosh = 20
gpa = 3.2
talaba = True
yosh = float(yosh)
ism = bool(ism)
print(ism)

#input() function
ism = input("What is your name:")
print(f"Salom {ism} yaxshimisiz?")
yosh = input("Necha yoshdasiz?:")
print(f"Siz {yosh} yoshdasiz ")

ism = input("Ismingiz nima:")
yosh = int(input("Necha yoshdasiz"))
yosh = yosh+1
print(f"Salom {ism}!")
print("Tug'ilgan kuningiz bilan")
print(f"Siz {yosh} yoshdasiz")

#Exercise 1 Rectangle Area
eni = float(input("Enini kiriting:"))
buyi = float(input("Bo'yini kiritng:"))
yuza = eni*buyi
print(f"Siz kiritgan to'rtburchakning yuzasi {yuza} ga teng!")
