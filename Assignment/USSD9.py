# registered = []


# def register():
#     global registered
#     num = input("Input your number: ")
#     registered = num
# max_attempt = 5
# attempt = 0
balance = 500

def check_airtime_balance():
    ussd_code = input("Input USSD code: ")
    if ussd_code[0] == "*" and ussd_code[4] == "#":
        print(f"Your airtime balance is {balance}")
    else:
        print("Incorrect USSD code.")

def transfer():
    much = int(input("How much do you want to transfer: "))
    if much <= balance:
        num = input("Enter Recipient's number: ")
        if len(num) == 11:
            print("Transfer successful!")
        else:
            print("Incorrect number.")
    else:
        print("Insufficient Airtime.")

def choice():
    print("""
                1. Check Airtime Balance
                2. Transfer
        """)
    choice = int(input("Choose an option (1-4): "))
    if choice == 1:
        check_airtime_balance()
    elif choice == 2:
        transfer()
    else:
        print("Incorrect")

def code():
    # while True:
    print("DIAL *555#")
    ussd_code = input("Input USSD code: ")
        # if ussd_code[0] == "*" and ussd_code[4] == "#":
    if ussd_code != "*555#":
        print("Incorrect USSD code.")
    else:
        choice()
        # else:
            # print("Incorrect USSD code.")
code()