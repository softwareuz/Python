while True:
    a = input("Raqam kiriting:")
    if a.isdigit():
        a = int(a)
        break
    print("Iltimos faqat raqam kiriting")


def juftmi(a):
    return "JUFT" if a % 2 == 0 else "TOQ"
print(juftmi(a))