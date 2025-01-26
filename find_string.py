user = input("Entter your name: ")
phone_number = input("Enter your phone number #:")
result = len(user) # count letter 
result1 = user.find(" ") # Find entered method case letter 
result2 = user.rfind("o") #Reverse find like matrix
result3 = user.capitalize() # upper case case only 1st character 
result4 = user.upper() # upper case all letter 
result5 = user.lower() # lower case all letter 
result6 = user.isdigit() # find only numbers boolean t or f
result6 = user.isalpha() #find only character boolean t or f
result7 = phone_number.count("-") #count "-"
result8 = phone_number.replace("-", "_")
print(result)
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
print(result7)
print(result8)
