# if "@" in email and email.endswith(".com")
email = input("Your E-mail: ")
# at_index = email.index("@")
at_index = email.find("@")
dotcom_index = email.find(".com")
# print(at_index)
# print(dotcom_index)
d = email[at_index + 1:dotcom_index]
print(d)



while True:
    email = input("Your E-mail: ").lower().strip()
    index_at = email.find("@")
    dotcomIndex = email.find(".com")
    text_btwn = email[index_at + 1:dotcomIndex]
    if "@" in email and email.endswith(".com"):
        if text_btwn.isalpha():
            print("Valid email...... Continue registration")
            break
        else:
            print("Invalid email....... Try again")
            continue
    else:
        print("Invalid email....... Try again")
        continue