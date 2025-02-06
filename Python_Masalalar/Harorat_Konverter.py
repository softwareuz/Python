"""
Selsiyda Berilgan Hararotni Farangeytga va aksincha Farangeytda berilgan haroratni selsiyga o'tkazish
"""
harorat = float(input("Haroratni kiriting: "))
birlik = input("C yoki F ni tanlang (C yoki F): ").strip().lower() #strip() va .lower() yordamida foydalanuvchi kiritgan katta kichik harflarni bir xil formatda qabul qilamiz
if birlik == 'c':
    F = (harorat * 9 / 5) + 32
    print(f"Siz Celsiyni Fahrenhaytga o'tkazdingiz. Natija: {F}°F")
elif birlik == 'f':
    C = (harorat - 32) * 5 / 9
    print(f"Siz Fahrenhaytni Celsiyga o'tkazdingiz. Natija: {C}°C")
else:
    print("Xato! Iltimos, faqat 'C' yoki 'F' kiriting.")


# Agar tushunmasangiz Telegramda @axrorback menga yozing .....