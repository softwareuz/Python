#format specifiers = {value: flags} foramt a value based on what flags are inserted
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
#:< = left justify
#:> = right justify
#^ = centr align
#+ = use a plus sign to indicate positive value
#= = place sign to indicate positive value
# = insert a space before positive numbers
# , = comma seperator
price1 = 12.345
price2 = 654.762
price3 = 5432.886665
print(f"Price 1 is: {price1:.2f}")
print(f"Price 2 is : {price2:.2f}")
print(f"Price 3 is : {price3:.2f}")