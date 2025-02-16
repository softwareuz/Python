def tub_sonmi(n):
    if n < 2:
        return False  # 2 dan kichik sonlar tub emas

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False  # Agar n biror songa bo‘linsa, tub emas

    return True  # Hech bir songa bo‘linmasa, tub son


# Foydalanuvchidan son olish
son = int(input("Sonni kiriting: "))
print(tub_sonmi(son))
