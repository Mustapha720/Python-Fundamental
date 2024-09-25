import random
questions = {
    "\nWhat is the capital of France?\n (a)Paris\n (b)New York\n (c)America\n (d)Washington": "a",
    "What has to be broken before you can use it?\n (a)Ball\n (b)Apple\n (c)Egg\n (d)Chair": "c",
    "Is 'print' an inbuilt python function?\n (a)Maybe\n (b)No\n (c)Yes\n (d)Neither": "c",
    "Which operator is used for exponentiation in Python?\n (a)^\n (b)*\n (c)%\n (d)**": "d",
    "______ is true when both operand are true?\n (a)AND\n (b)NOT\n (c)OR\n (d)XOR": "a",
    "What variable convention is this 'NameOfStudent'?\n (a)Camel casing\n (b)Snake casing\n (c)Pascal casing\n (d)Donkey casing": "c",
    "Python is ______ language?\n (a)Not a language\n (b)A High-level language\n (c)A Low-level language\n (d)Don't know": "b",
    "How do you insert an element into a list in Python?\n (a)list.add()\n (b)list.push()\n (c)list.append()\n (d)list.extend()": "c",
    "What is the correct way to check if two values are equal in Python?\n (a)==\n (b)=\n (c)!=\n (d)===": "a",
    "Which of the following data types is mutable in Python?\n (a)Tuple\n (b)String\n (c)Int\n (d)List": "d"
}


list_of_student=[]
registered_students = {}

for each in range(1,6):
    student_name= input("Your Name: ")
    student_matric_number= input("Your Matric Number: ")
    print("Registration Successful")
    registered_students[student_name]= student_matric_number
print(registered_students)

for name in registered_students.keys():

    if name in list_of_student:
        continue
    next_student = input(f"Is {name} ready for the test? (Yes/No): ").strip().lower()
    
    if next_student != "yes":
            print(f"{name} is not ready.")
            continue
    student_matric_number = input(f"{name}, Your Matric Number: ")
    
    if student_matric_number != registered_students[name]:
        print(f"{name}, Your Matric Number is incorrect.")
        continue
    
    if name in list_of_student:
        print(f"{name}, You've already taken the exam.")
        continue

    list_of_student.append(name)

    ready = input(f"{name}, Are you ready to take the exam? (Yes/No): ").strip().lower()

    if ready != "yes":
        print(f"{name}, You are not ready to take the exam, come when you are ready.")
        continue

    score=0
    random_questions = random.sample(list(questions.items()), 5)
    
    for question, answer in random_questions:
        print(question)
        user_answer=input('Your answer: ').strip().lower()

        if user_answer == answer:
            score+=10

    print(f'Your total score is {score} / 50')

    if each < 4:
        next_student = input("Is the next student ready? (Yes/No): ").strip().lower()
        if next_student != "yes":
            print("Test Terminated")
            break