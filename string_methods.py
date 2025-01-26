#Validate user input Exercises
#1. username is no more 12 characters
#2. username must not contain spaces
#3. username must not contain digits

# 1 Exercise username is not more 12 characters
username = input("Enter your username: ")
if len(username) > 12:
    print("username must be contain 12 charater try again!")
elif not username.find(" ") == -1:
    print("Check again without spaces")
elif not  username.isalpha():
    print("Try again without digits")
else:
    print(f"Welcome {username}")
