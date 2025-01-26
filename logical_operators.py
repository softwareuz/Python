# Topic : Logical Operators
# or at least one condition must be true
# and both condition must be true
# not inverse condition (not False not True)

# Exercise 1 or
temp = 25
is_raining = False
if temp > 30 or temp < 0 or is_raining: 
    print("The outdor Event Canceled")
else:
    print("The outdoor Event still Scheduled!")

#Exercise 2 and
temp = -28
is_sunny = True
if temp >= 28 and temp <= 35 and is_sunny:
    print("The outside very Hot")
    print("Very Sunny")
elif temp < 0 and is_sunny:
    print("The outside Very Cold")
else:
    print("The Outside Not Sunny")

