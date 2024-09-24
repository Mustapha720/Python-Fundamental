def landing_page():
    print("""
            1. Login
            2. Register
            3. Make enquiry
            4. EXIT
        """)
    user=input('Select option: ')
    if user == "1":
        print("WELCOME")
    elif user == '2':
        print("WELCOME!!! You can now register")
    elif user == '3':
        print("What do you want? ")
    elif user == '4':
        exit()
landing_page()