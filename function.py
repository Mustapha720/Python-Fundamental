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

"""
Parameterized Function
Non-parameterized Function
Global Variable
Local Variable
Parameter
Arguments
"""

z = 10

# def add_num(x):
#     sum_num = x + 6
#     print(sum_num)
# add_num(4)

# def add_num(x, y):
#     global b
#     b = 25
#     q = 18     # Local variable
#     sum_num = x + 8 + y + z + q
#     print(sum_num)
# add_num(4, 2)

# def subtract_all(j, k):
#     sub_all = b - j - 8 - k - z
#     print(sub_all)
# subtract_all(15, 2)

"""
Types of arguments
1. Default arguments
2. Keyword arguments
3. Positional arguments
4. Arbitrary arguments
"""

# # 1. Default arguments
# def add_num(x, y=14):
#     global b
#     b = 25
#     q = 18     # Local variable
#     sum_num = x + 8 + y + z + q
#     print(sum_num)
# add_num(4, 10)

# # 2. Keyword arguments
# def college(name, location):
#     print(name, location)
# college(name="SQI", location="Yoaco")
# college(location="Yoaco", name="SQI")

# # 3. Positional arguments
# def college_level(college, level):
#     print(f"My name is Dara, I study at {college} and my level is {level}")
# college_level("SQI", "Level 2")
# college_level("Level 2", "SQI")

# # 4. Arbitrary arguments
# # arbitrary args
# def college_level(*args):
#     print(f"My name is Dara, I study at {args[0]} and my level is {args[1]}, I'm about to go {args[2]}")
# college_level("SQI", "Level 2", "home", "Titi", "Boluwatife")

# arbitrary kwargs
def college_level(**kwargs):
    print(kwargs.keys())
    print(kwargs.values())
    print(kwargs.items())
    name, level, *other = kwargs
    print(f"My name is {name}")
college_level(name="SQI", level="Level 2", address="home", name1="Titi", name2="Boluwatife")










"""
# Simulate a basic database to store users
users_db = {}

# Function to register users
def register(username, password):
    if username in users_db:
        return "Username already exists!"
    users_db[username] = {
        'password': password,
        'score': None  # Score is initially set to None
    }
    return "Registration successful!"

# Function to login users
def login(username, password):
    if username not in users_db:
        return "Username does not exist!"
    if users_db[username]['password'] == password:
        return "Login successful!"
    else:
        return "Incorrect password!"

# Function for the CBT exam
def take_exam(username):
    if username not in users_db:
        return "Please register first!"

    if users_db[username]['score'] is not None:
        return f"{username}, you have already taken the exam. Your score is {users_db[username]['score']}."

    # Simple mockup exam with 3 questions
    questions = [
        ("What is 2 + 2?", 4),
        ("What is the capital of France?", "Paris"),
        ("What is the color of the sky?", "Blue")
    ]

    score = 0

    for question, correct_answer in questions:
        print(question)
        user_answer = input("Your answer: ")  # In real applications, replace with UI logic
        if str(user_answer).strip().lower() == str(correct_answer).strip().lower():
            score += 1

    users_db[username]['score'] = score
    return f"{username}, you scored {score}/{len(questions)}!"

# Simulate 5 applicants taking the exam
def start_exam():
    for i in range(5):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if login(username, password) == "Login successful!":
            print(take_exam(username))
        else:
            print("Invalid login. Try again.")

# Example: Register 5 applicants
for i in range(5):
    username = input(f"Register User {i+1}, enter a username: ")
    password = input(f"Register User {i+1}, enter a password: ")
    print(register(username, password))

# Example: Login and start CBT exam
start_exam()
"""