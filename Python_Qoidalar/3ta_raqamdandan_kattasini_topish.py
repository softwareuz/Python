"""
Python Dasturlash tilida 3 ta raqamdan eng katta sini topish 2 xil uslubda ko'rib chiqamiz
"""
son1 = int(input("1-sonni kiriting:"))
son2 = int(input("2-sonni kiriting:"))
son3 = int(input("3-sonni kiriting:"))

print(f"Siz kiritgan raqamlarning eng kattasi: {max(son1 , son2 , son3)}") #Qulay yo'llardan biri max keywordidan foydalanish


# 2-yo'l operatorlardan foydalanamiz
print("Shu yerdan pastki qismda if yordamida yozilgan kod natijasi konsolga chiqadi") # Bu qator kodda ishlamaydi shunchaki chalg'imaslik uchun yozmasangiz ham bo'ladi
if son1 > son2 and son1 > son3:
    print(f"Eng katta son {son1}")
elif son2 > son1 and son2 > son3:
    print(f"Eng katta son {son2}")
elif son3 > son1 and son3 > son2:
    print(f"Eng kata son {son3}")
else:
    print("Bu sonlar o'zaro Teng")

# Siz o'zingizga qulay yo'ldan foydalanishingiz mumkin


# Topshiriq 3 ta raqamdan eng kichigini topuvchi dastur kodini Python dasturlash tilida yozing