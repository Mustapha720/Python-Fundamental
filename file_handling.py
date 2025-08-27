# File handling
myfile="example1.txt"

# with open(myfile, "w") as file:
    # file.write("helooooooooooooo")
    # print('text written successfully')

# with open(myfile, "a") as file:
    # file.write("you are welcome")
    # print('text written successfully')

# with open(myfile, "r") as file:
#     content=file.read()
#     print(content)

# with open(r"C:\Allproject\example3.pdf", "r") as file:
#     # file.write("mr emma is unhappy because his baby mama did  not cook for him")
#     content=file.read()
#     # print('done')
#     print(content)

# with open(r"C:\Users\Lenovo\Pictures\waetherf\clear-w.jpg", "rb") as file:  
#     data = file.read()
#     print(data)

# with open(r"C:\Users\Lenovo\Downloads\sqi.csv", "r") as file:  
#     data = file.read()
#     print(data, "an excel file") #this will throw an error becos  Python has encounter characters in the file that it cannot decode

# READING EXCEL FILE
# with open(r"C:\Users\Lenovo\Downloads\sqi.csv", "r", encoding='utf-8') as file:  
#     data = file.read()
#     print(data, "an excel file")

# with open("example2.pdf", "r+") as file:
#     content = file.read()  # Read the entire file content
#     file.seek(0, 2)  # Move the file pointer to the end of the file
#     file.write("this mode is a special mode\n")  # Write to the file
#     file.seek(0)  # Move the file pointer back to the beginning
#     updated_content = file.read()  # Read the file again to get updated content
#     print(updated_content)

# with open("example2.pdf", "a+") as file:
#     file.write("this mode is a special mode\n")  # Append the text
#     file.seek(0)  # Move the file pointer to the beginning
#     updated_content = file.read()  # Read the entire file content
#     print(updated_content)  # Print the updated content

# try:
#     with open("example4.html", "a") as file:

#         file.write("<h5>this file is opened using python</h5>")
#         print("file created")
#         # print(file.read())
# except FileExistsError:
#     print("File already exists!!!")

import os
# os.mkdir(r'C:\python_pclass\newfolder1')   #
# print("done")
# os.mkdir('C:\\python-pclass\\goodness\\example4.pdf')
# print("done")
# myfile2='example6.csv'
# with open(r'C:\\python_pclass\\newfolder1\\myfile2', 'r', encoding='utf-8') as file:
#     # file.write("creating a new file using the x mode")
#     print(file.read())
    # print('done')

# all_folder=os.listdir(r"C:\\python_pclass")
# for all in os.listdir(r"C:\\python_pclass"):
#     print(all)

# with os.scandir(r'C:\\python_pclass') as entries:
#     for entry in entries:
#         print(entry.name)


# # Check if the directory already exists
# directory_path='folder3'
# if not os.path.exists(directory_path):
#     # If it doesn't exist, create it
#     os.makedirs(directory_path)
#     print("Directory created successfully")
# else:
#     print("Directory already exists")

# class  work: create a directory in your current directory and any other path of your choice, insert a file and write in it. 

# folds=os.makedirs(r'folder1/folder2/folder3')
# print(folds)
# print('done')





# entries = os.listdir("C:\\python_pclass")
# for entry in os.listdir("C:\\python_pclass"):
#     print(entry)
# # # Specify the directory path
# directory_path = 'C:\\python-pclass\\goodness'

# # Check if the directory already exists
# if not os.path.exists(directory_path):
#     # If it doesn't exist, create it
#     os.makedirs(directory_path)
#     print("Directory created successfully")
# else:
#     print("Directory already exists")

# # Now, specify the file path within the directory
# file_path = os.path.join(directory_path, 'example4.pdf')

# # Check if the file already exists
# if not os.path.exists(file_path):
#     # If it doesn't exist, create it
#     with open(file_path, 'w') as file:
#         # You can optionally write something to the file
#         file.write("This is a PDF file created using Python!")
#     print("File created successfully")
# else:
#     print("File already exists")

list_item=["1", "2", "rice"]