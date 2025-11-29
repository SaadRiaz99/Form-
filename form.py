user = {}

while True:
    print("\n=== Welcome to our Form ===")
    print("1. Create Account")
    print("2. Login")
    print("3. Show All Users")
    print("4. Exit Form")

    Chose = int(input("Enter Your Number: "))

    # CREATE ACCOUNT
    if Chose == 1:
        a = input("Enter Your Name: ")
        if a in user:
            print("============= Username Already Exists =============")
        else:
            passw = input("Enter Your Password: ")
            user[a] = passw
            print(" Congratulations! Your account has been created successfully.")

    # LOGIN
    elif Chose == 2:
        username = input("Enter Username: ")
        password = input("Enter Password: ")

        if username in user and user[username] == password:
            print(f" Login Successful! Welcome {username}!")
        else:
            print(" Username doesn't exist or invalid password.")

    # SHOW USERS
    elif Chose == 3:
        print("\n=== All Registered Users ===")
        if user:
            for name in user:
                print("-", name)
        else:
            print(" No users found. Please create an account first.")

    # EXIT
    elif Chose == 4:
        print("👋 Allah Hafiz!")
        break

    # INVALID INPUT
    else:
        print(" Invalid choice, please try again.")
