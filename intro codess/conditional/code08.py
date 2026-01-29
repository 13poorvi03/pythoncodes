username = input("Enter username: ")
password = input("Enter password: ")

if username == "Poorvi":
    if password == "python123":
        print("Login successful ✅")
    else:
        print("Wrong password ❌")
else:
    print("Unknown user ❌")