"""
list
tuple
set
dictionary
"""
# Creating a list in python
list_of_item= ['1', 3j, 6.8, True, ['Temi', 'Taiwo']]
list_of_student= (['kiki', 'bolu', 'tope', ['dara', 'dray']])
list_of_student1= (['kiki', 'bolu', 'tope', ['dara', 'dray'], 'kiki', 'bolu', 'tope'])
list_of_student2= ([['kiki', 'bolu', 'tope'], ['dara', 'dray'], ['kiki', 'bolu', 'tope']])

# print(type(list_of_item))
# print(type(list_of_student))
# print(type(list_of_student1))

# print(len(list_of_student1))
# print(len(list_of_student))
# print(len(list_of_item))

# print(list_of_student1[3][1])
# print(list_of_student2[0][1], list_of_student2[1][0])

# print(list_of_student1[::-1]) # reversing
# list_of_student1.reverse()
# print('Reversing/flipping all the names: ', list_of_student1) # reversing


# list_of_student2.append('Dara')
# list_of_student2.append('Darasimi')
# print('Appending a name: ', list_of_student2)

# Classwork
# Collect 5 student name and age, store them in a variable and display the content of the variable in your terminal
"""
MY METHOD:

name_of_student1=input("Your name: ")
age_ofStudent1=input("Your age: ")
name_of_student2=input("Your name: ")
age_ofStudent2=input("Your age: ")
name_of_student3=input("Your name: ")
age_ofStudent3=input("Your age: ")
name_of_student4=input("Your name: ")
age_ofStudent4=input("Your age: ")
name_of_student5=input("Your name: ")
age_ofStudent5=input("Your age: ")
print('The', age_ofStudent1, 'years old', name_of_student1, 'is a student')
print('The', age_ofStudent2, 'years old', name_of_student2, 'is a student')
print('The', age_ofStudent3, 'years old', name_of_student3, 'is a student')
print('The', age_ofStudent4, 'years old', name_of_student4, 'is a student')
print('The', age_ofStudent5, 'years old', name_of_student5, 'is a student')
"""

"""
list_of_student=[]

for each in range(0, 3):
    name=input('Your name: ')
    age=input('Your age: ')
    age_name= name, age
    list_of_student.append(age_name)
    print(list_of_student)


for each in range(0, 3):
    age_name= [input('Your name: '), input('Your age: ')]
    list_of_student.append(age_name)
    print(list_of_student)
"""


# list_of_student3= [['Aliu', 'Habeeb','Fathima'], ['Sodiq', 'Toheeb']]
# list_of_student1.extend(list_of_student3)
# print(list_of_student1)
# list_of_student1.insert(2, 'Mustapha')
# print(list_of_student1)

# list_of_student1.remove('kiki')
# # print(list_of_student1)
# list_of_student1.pop()
# list_of_student1.pop(1)
# print(list_of_student1)


# For list of integer
# lst1= []
# lst1= [int(item) for item in input("Enter the list items: ").split()]
# print(lst1)

# lst1.sort()
# print(lst1)