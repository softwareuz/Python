while True:
    a = input("Juft yoki toqlikni tekshirish uchun raqam yozing:") .strip()
    if a.isdigit():
        a = int(a)
        break
    print("Iltimos faqat raqam kiriting!!!")
if a % 2 == 0:
    print(f"Siz kiritgan raqam {a} va bu JUFT raqam hisoblanadi")
else:
    print(f"Siz kiritgan  raqam {a} va bu raqam TOQ raqam hisoblanadi")
