son = int(input("Sonni kiriting: "))

# Raqamlar yig‘indisini hisoblash
yigindi = 0
while son > 0:
    yigindi = yigindi + son % 10  # Oxirgi raqamni olish va yig‘indiga qo‘shish
    son //= 10  # Sonni bitta raqam kamaytirish

# Natijani chiqarish
print(f"Raqamlar yigindisi: {yigindi}")
