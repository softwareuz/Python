"""
Python Dasturlash tilida Funksiyalar Mavzusi
"""
#def kalit so'zi yordamida funksiyalar yasab ko'ramiz

# 1-sodda misol ekranga Assalomu Alrykum yozuvini slom_ber funksiya nomi orqali chiqarish

def salom_ber(): #salom_ber bu yerda funksiya ismi
    print("Assalomu Aleykum") # slom_ber funksiya chaqirilganda ekranga chiqadigan qiymat
salom_ber() #funksiyani ekranga chaqarish

# 2-misol
print("Salom")
def kvadrat_hisoblash(a):
    return a**2
natija = kvadrat_hisoblash(3)
print(natija)
# Kodimizni yaxshilaymiz ozgina

x = int(input("Son kiriting:"))
def kvadrat(x):
    return x**2
print(f"Siz kiritgan sonning kvadrati {kvadrat(x)} ga teng")

# 3-misol yig'indi  *args cheksiz argumentlar
def yigindi(*sonlar): #Cheksiz argumentlar
    return sum(sonlar)  # Barcha sonlarni qo‘shadi

print(yigindi(1, 2, 3, 4, 5))  # Natija: 15

# 4-misol **kwargs kalit-qiymat juftliklarini qabul qilish
def shaxs_info(**malumotlar):
    for kalit, qiymat in malumotlar.items():
        print(f"{kalit}: {qiymat}")

shaxs_info(ism="Axror", yosh=20, kasb="Dasturchi")
