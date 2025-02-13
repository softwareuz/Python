# Indxing-accesing elements of a squence using [] indexing operator
#                           [ start : end : step ]

card_number = "1234-5678-9012-3456"
print(card_number[0])
print(card_number[: 4])
print(card_number[0 : 4])
print(card_number[5 : 9])
print(card_number[5 : ])
print(card_number[-1])
print(card_number[: : 2])
last = card_number[-4 : ]
print(f"XXXX-XXXX-XXXX-{last}")
