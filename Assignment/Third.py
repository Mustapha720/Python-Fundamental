# 1. Build even and odd number checker
# 2. Collect names of student and group them into two different department
# 3. Set five structural CBT question and grade the student

"""
1.
number = int(input("Enter a number: "))
if  number  % 2 == 0:
    print("The number you entered is an even number")
else:
    print("The number you entered is an odd number")
"""

"""
2.
name = input("Enter your name: ")
if len(name) % 9 == 4:
    print('You are a Cyber security student')
else :
    print('You are a Web developer')
"""


# 2.
# name=input("What is your name?: ")
# yourName=input("What is your name?: ")

# if (len(name) > len(yourName)):
#     print("He/She is in CIT department")
# else:
#     print("He/She is in Python department")


"""
3.
score=0
question=input('1. The capital of Oyo state is?: ')
ans=['Ibadan', 'ibadan']
if question in ans:
    score+=5
    print('Correct')
else:
    print('Oh noo! You got it wrong')

question=input('2. Is "print" an inbuilt python function?: ')
ans=['Yes', 'yes']
if question in ans:
    score+=5
    print('Correct')
else:
    print('Oh noo! You got it wrong')

question=input('3. Is "chair" a fruit?: ')
ans=['No', 'no']
if question in ans:
    score+=5
    print('Correct')
else:
    print('Oh noo! You got it wrong')

question=input('4. What is the full meaning of IDE?: ')
ans=['Integrated Development Environment', 'integrated development environment']
if question in ans:
    score+=5
    print('Correct')
else:
    print('Oh noo! You got it wrong')

question=input('5. Is USA a county?: ')
ans=['Yes', 'yes']
if question in ans:
    score+=5
    print('Correct')
else:
    print('Oh noo! You got it wrong')

question=input('6. What is the capital of USA?: ')
ans=['Washington, D.C', 'washington', 'Washington']
if question in ans:
    score+=5
    print('Correct')
else:
    print('Oh noo! You got it wrong')

question=input('7. What has keys but cannot open locks?: ')
ans=['Piano', 'piano', 'A piano', 'a piano']
if question in ans:
    score+=5
    print('Correct')
else:
    print('Oh noo! You got it wrong')

question=input('8. What has to be broken before you can use it?: ')
ans=['An egg', 'an egg', 'egg', 'Egg']
if question in ans:
    score+=5
    print('Correct')
else:
    print('Oh noo! You got it wrong')

question=input('9. What comes down but never goes up?: ')
ans=['Rain', 'rain']
if question in ans:
    score+=5
    print('Correct')
else:
    print('Oh noo! You got it wrong')

question=input('10. I have branches, but no fruit, trunk, or leaves. What am I?: ')
ans=['A bank', 'a bank', 'bank', 'Bank']
if question in ans:
    score+=5
    print('Correct')
else:
    print('Oh noo! You got it wrong')

print('Total',score)
"""




# Define questions and correct answers
"""
questions = [
    "1. What is the capital of France?",
    "2. What is the square root of 16?",
    "3. Who wrote the play 'Romeo and Juliet'?",
    "4. What is the chemical symbol for water?",
    "5. How many continents are there on Earth?"
]

correct_answers = [
    "paris",          # 1. Capital of France
    "4",              # 2. Square root of 16
    "shakespeare",    # 3. Author of "Romeo and Juliet"
    "h2o",            # 4. Chemical symbol for water
    "7"               # 5. Number of continents on Earth
]

# Function to grade the student's answers
def grade_student(answers):
    score = 0
    total_questions = len(questions)
    
    # Compare student's answers with correct answers
    for i in range(total_questions):
        if answers[i].strip().lower() == correct_answers[i]:
            score += 1
    
    # Calculate the grade percentage
    grade = (score / total_questions) * 100
    return score, grade

# Sample student answers
student_answers = [
    input(questions[0] + " "),  # Collect answers from the student
    input(questions[1] + " "),
    input(questions[2] + " "),
    input(questions[3] + " "),
    input(questions[4] + " ")
]

# Grade the student's answers
score, grade = grade_student(student_answers)

# Output the result
print(f"\nYou got {score} out of {len(questions)} correct.")
print(f"Your grade is: {grade:.2f}%")
"""