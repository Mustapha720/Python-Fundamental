questions = {
    "\n1. What is the capital of France?\n (a)Paris\n (b)New York\n (c)America\n (d)Washington": "a",
    "2. What has to be broken before you can use it?\n (a)Ball\n (b)Apple\n (c)Egg\n (d)Chair": "c",
    "3. Is 'print' an inbuilt python function?\n (a)Maybe\n (b)No\n (c)Yes\n (d)Neither": "c",
    "4. Which operator is used for exponentiation in Python?\n (a)^\n (b)*\n (c)%\n (d)**": "d",
    "5. ______ is true when both operand are true?\n (a)AND\n (b)NOT\n (c)OR\n (d)XOR": "a",
    "6. What variable convention is this 'NameOfStudent'?\n (a)Camel casing\n (b)Snake casing\n (c)Pascal casing\n (d)Donkey casing": "c",
    "7. Python is ______ language?\n (a)Not a language\n (b)A High-level language\n (c)A Low-level language\n (d)Don't know": "b",
    "8. How do you insert an element into a list in Python?\n (a)list.add()\n (b)list.push()\n (c)list.append()\n (d)list.extend()": "c",
    "9. What is the correct way to check if two values are equal in Python?\n (a)==\n (b)=\n (c)!=\n (d)===": "a",
    "10. Which of the following data types is mutable in Python?\n (a)Tuple\n (b)String\n (c)Int\n (d)List": "d"
}


list_of_student={}

for each in range(1,6):
    student_name= input("Your Name: ")
    student_matric_number= input("Your Matric Number: ")
    list_of_student[student_matric_number]= student_name
print(list_of_student)

for each in range(1,6):
    student_matric_number = input("Your Matric Number: ")

    if student_matric_number not in list_of_student:
        print(f"You have not registered\n")
        continue
    are_you_ready = input("Are you ready to do your exam? (Yes/No): ").strip().lower()
    if are_you_ready !='yes':
        print('Test terminated.')
        continue

    score=0
    for question, answer in questions.items():
        print(question)
        user_answer=input('Your answer: ').strip().lower()

        if user_answer == answer:
            score+=10

    print(f'Your total score is {score} / 100')

    if each < 4:
        next_student = input("Is the next student ready? (Yes/No): ").strip().lower()
        if next_student != "yes":
            print("Test Terminated")
            break