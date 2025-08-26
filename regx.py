import re

email = "bola@gmail.com"
# if email.endswith('.com'):
#     print('Valid email')
# else:
#     print('Invalid email')


val_search = re.search("^@gmail.*com$", email)
if val_search:
    print("valid email")
else:
    print("Invalid email")