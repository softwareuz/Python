a = int(input("a ni kiriting:"))
b = int(input("b ni kiriting:"))
c = int(input("c ni kiriting:"))

def kattasi(a , b , c):
    if a == b == c:
        return " Bu Sonlar Teng"
    max_sonlar = max(a , b , c)
    if max_sonlar == a:
        return "A katta"
    elif max_sonlar == b:
        return "B katta"
    else:
        return "C katta"

print(kattasi(a , b , c))