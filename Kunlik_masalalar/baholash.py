while True:
    a = input("qiymat kiriting(0-100):")
    if a.isdigit():
        a = int(a)
        if 0 <= a <= 100:
            break
    print("Iltimos qayta urunib ko'ring")

if 90 < a > 100:
    print("A'lo")
elif 70 < a > 89:
    print("Yaxshi")
elif 50 < a > 69:
    print("O'rtacha")
elif 0 < a > 49:
    print("YOMON")