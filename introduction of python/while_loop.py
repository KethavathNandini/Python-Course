password = "smile"
while True:
    user_password = input("enter your password: ")
    if user_password == password:
        print("your password is correct")
        break
    else:
        print("your password is wrong")
print("logged in!")