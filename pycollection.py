"""
list
tuple
set
dictionary
"""


# LIST
# Creating a list in python
# list_of_item= ['1', 3j, 6.8, True, ['Temi', 'Taiwo']]
# list_of_student= (['kiki', 'bolu', 'tope', ['dara', 'dray']])
# list_of_student1= (['kiki', 'bolu', 'tope', ['dara', 'dray'], 'kiki', 'bolu', 'tope'])
# list_of_student2= ([['kiki', 'bolu', 'tope'], ['dara', 'dray'], ['kiki', 'bolu', 'tope']])

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





"""
# TUPLE
# fruits=('mango','pawpaw')
# fruits1=tuple(('mango','pawpaw'))
# fruits2=('mango','pawpaw', 3j, ('dara', 'temi', 'taiwo'), ['banana', 'apple'], {1, 2, 3, 4,})
# fruits3=(('mango','pawpaw','cashew'), ('mango','pawpaw'), ())
# print(type(fruits))
# print(type(fruits1))
# print(len(fruits1))
# print(fruits2[::2])
# print(type(fruits2))
# print(len(fruits2))
# print(fruits2[3])

# for name in fruits2[3]:
#     print(name)


# empolyee=(('Dara', 'mustymoney@gmail.com', 'Jin_Tempest', 'Male'), ('Taiwo', 'taiwo123@gmail.com', 'liegeman', 'Male'), ('Temi','iyagbogbo@gmail.com','Tom_boy','Female'), ('Dara', 'mustymoney@gmail.com', 'Jin_Tempest', 'Male'))

# empolyee1, *others, empolyee3 = empolyee
# print(empolyee1)
# print(others)
# print(empolyee9)

# empolyee1, empolyee2, empolyee3 = empolyee
# print(empolyee)

# for name, email, username, gender in empolyee:
#     print('Name: ',name)
    # print('Email: ',email)
    # print('User_Name: ', username)
    # print('Gender: ', gender)

x=0
# for _, email, _, _ in empolyee:
x+=1
#     print('Name: ',name)
    print('Email: ', {x},email)
    # print('User_Name: ', username)
    # print('Gender: ', gender)

# concatenation in tuple
# fruits3= fruits + fruits1
# print(fruits3)

# Deleting in tuple
# print(fruits2)
# del fruits2
# print(fruits2)
"""




"""
# SET
set1={1, 4,6, 2}
set2=set((1, 2, 3, 4))
# set1={1, 2, 3, 4}
# print(type(set1))
# print(type(set2))
# set1.add(56)
# set1.update((56, 79))
# set1.remove((79))
# print(set1)
# set3=set1.copy()
# set3=set1.intersection(set2)
# set3=set1.difference(set2)
# set3=set1.issubset(set2)
# print(set3)
"""







# DICTIONARY
# How to create a dictionary
electronic={"Laptop" : "Lenovo", "Phone" : "Samsung", "MIFI": "MTN", "Car": "BMW i4",}
electronic1=dict([(1, "HP"), (2, "DEL")])
electronic2=dict(fruit="mango", fruit1="orange")
# electronic.popitem()
# electronic.pop("Laptop")
# del electronic["MIFI"]
# print(electronic)
# print(type(electronic))
# print(type(electronic1))
# print(electronic1[2])
# print(electronic1.keys())
# print(electronic1.values())
# print(electronic1.items())
# print(electronic["Laptop"])

# for keys, values in electronic.items():
    # print(keys)

# electronic.update(dict(year=2023, color="white"))
# electronic.update(dict(year=2024, color="black"))
# print(electronic)


score=0
questions={input("What is the capital of nigeria a) ogbomoso  b) abuja" ): 'b'}
# value={input("Your answer: ")}
for values in questions.items:
    score+=5
    print("correct")
else:
    print('n')