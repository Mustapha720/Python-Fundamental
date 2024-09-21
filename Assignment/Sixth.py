student1=input('Your name: ')
pass_word1=input("Your password: ")
student2=input('Your name: ')
pass_word2=input("Your password: ")
student3=input('Your name: ')
pass_word3=input("Your password: ")
student4=input('Your name: ')
pass_word4=input("Your password: ")
student5=input('Your name: ')
pass_word5=input("Your password: ")

exam=input("\n \nAre you ready to take the exam now? ")
ans=('Yes', 'yes')
if exam in ans:
    pass
else:
    quit("")
    # break


student=input('\nYour name: ')
pass_word=input("Your password: ")
pass_words=('Dara1', 'dara1', 'Temi', 'temi', 'taiwo', 'Taiwo', 'dara', 'Dara')
if pass_word in pass_words:
    print('You are qualified to take the exam')
    pass
else:
    print('Incorrect password.')
    quit("")





questions = {
    "1. What is the capital of France?\n (a)Paris\n (b)New York\n (c)America": "a",
    "2. What has to be broken before you can use it?\n (a)Ball\n (b)Apple\n (c)Egg": "c",
    "3. Is 'print' an inbuilt python function?\n (a)Maybe\n (b)No\n (c)Yes": "c",
    "4. What is the full meaning of IDE?\n (a)Independent\n (b)Integrated Development Environment\n (c)IDE": "b",
    "5. ______ is true when both operand are true?\n (a)AND\n (b)NOT\n (c)OR": "a",
    "6. What variable convention is this 'NameOfStudent'?\n (a)Camel casing\n (b)Snake casing\n (c)Pascal casing": "c",
    "7. Python is ______ language?\n (a)Not a language\n (b)A High-level language\n (c)A Low-level language": "b",
    "8. ": "",
    "9. ": "",
    "10. ": ""
}

score=0
for question, answer in questions.items():
    print(question)
    user_answer = input("Your answer: ").lower()

    if answer in user_answer:
        score+=10
        print('Correct')
    else:
        print('Wrong')

print(f"Your total score is {score} / 100")






"""
# CBT Example: Questions and Answers in a Dictionary

# Displaying instructions
print("Welcome to the Computer-Based Test (CBT)")
print("Please answer the following questions:\n")

# Dictionary to store questions and answers
questions = {
    "What is the capital of France?": "paris",
    "What is the square root of 64?": "8",
    "Who wrote 'Hamlet'?": "shakespeare"
}

# Variable to keep track of score
score = 0

# Loop through the dictionary and ask each question
for question, correct_answer in questions.items():
    print(question)  # Print the question
    user_answer = input("Your answer: ").lower()  # Get user's answer and make it lowercase

    # Check if the answer is correct
    if user_answer == correct_answer:
        print("Correct!\n")
        score += 1  # Increase the score if the answer is correct
    else:
        print(f"Wrong! The correct answer is {correct_answer.capitalize()}.\n")

# Final score and summary
print(f"Test completed. You got {score} out of {len(questions)} correct!")
"""






















# question={input('What is the capital of Nigeria? \n(a)Tokyo \n(b)Ibadan \n(c)Abuja'): 'b'}
# ans=input("Your answer: ")
# for values in ans:
    # print('Correct')
# else:
    # print("n")
# if values not in ans:
    # print('Wrong')