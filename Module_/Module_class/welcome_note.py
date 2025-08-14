def welcome(name):
    print(f"{name}, thank you for joining! An e-mail will be sent to you shortly.")



def wel(*names):
    # all_user = ", ".join(name)
    all_user = ", ".join(str(name) for name in names)
    print(f"{all_user}, thank you for joining! An e-mail will be sent to you shortly.")