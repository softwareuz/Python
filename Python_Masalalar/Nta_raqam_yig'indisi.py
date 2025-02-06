"""
Python Dasturlash tilida 1dan N gacha bo'lgan sonlar yig'indisini hisoblash
"""
def sum_numbers(n):
    return (n*(n+1))//2 #Matematik formula yordam eng oson yo'l shu deb o'yladim S = (n*(n+1))/2  Bu yerda // sonni butun qismini olish uchun ishlatildi
n = int(input("N ni kiriting:")) # N ga qiymat kiritsangiz 1 dan N gacha bo'lgan sonlarni yig'indisini hisoblaydi
print("Yig'indi:",sum_numbers(n))