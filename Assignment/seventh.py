student = []
# registered_student = []

def Register():
    for each in range(1):
        name = input("Your Name: ")
        matric_number = input("Your Matric Number: ")
        students = name, matric_number   
        student.append(students)
        global student
    print(student)
Register()

def Ready_or_Not():
    ready = input("Are you ready to take the exam? (Yes/No): ").strip().lower()
    if ready == "yes":
        are_you_ready = input("Your Matric Number: ")
        if are_you_ready not in student:
            print('You have not register')
        else:
            print("fsdfghd")
Ready_or_Not()

# def landing_page():
#     print("""
#             1. Login
#             2. Register
#             3. Make enquiry
#             4. EXIT
#         """)
#     user=input('Select option: ')
#     if user == "1":
#         print("WELCOME")
#     elif user == '2':
#         print("WELCOME!!! You can now register")
#     elif user == '3':
#         print("What do you want? ")
#     elif user == '4':
#         exit()
# landing_page()