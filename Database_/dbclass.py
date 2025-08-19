# pip install pymysql

# import decouple import config
import os
import pymysql as pyms
from dotenv import load_dotenv
load_dotenv()

dbPass = os.getenv("DB_PASS")

my_con = pyms.connect(host = '127.0.0.1', user = 'root', password = dbPass, db = "DatabaseIntro")
# my_con = pyms.connect(host = '127.0.0.1', user = 'root', password = config('dbPass'))
# print('Connection Successful')


myCursor = my_con.cursor() # Messenger between pc and sql 
# print("Done")

# myCursor.execute("CREATE DATABASE DatabaseIntro") # Create a database
# print('Successfully Created')

# myCursor.execute("CREATE TABLE Registration_Table (std_id INT(4), full_name VARCHAR(30), address VARCHAR(50), password VARCHAR(20))") # Table Creation
# print('Table created')


# Query to fetch database
# myCursor.execute("SHOW DATABASES")
# for db in myCursor:
#     print(db)
# myCursor.close()

# Checking columns
# myCursor.execute("SHOW COLUMNS FROM Registration_Table")
# for col in myCursor:
#     # print(col[0])
#     print(col)
# myCursor.close()


# ALTER: ADD, DROP, CHANGE & MODIFY
# MODIFY
# my_query = "ALTER TABLE Registration_Table MODIFY full_name VARCHAR(30) AFTER password"
# myCursor.execute(my_query)
# CHANGE
# my_query = "ALTER TABLE Registration_Table CHANGE std_id student_id INT(5) PRIMARY KEY AUTO_INCREMENT"
# myCursor.execute(my_query)
# ADD
# my_query = "ALTER TABLE Registration_Table ADD phone_num VARCHAR(11) UNIQUE"
# myCursor.execute(my_query)
# print('Done')


# Populate the table/Add one user (%s is a placeholder)
# my_query = "INSERT INTO Registration_Table (address, password, full_name, phone_num) VALUES(%s, %s, %s, %s)"
# value = ("Baby", "1234", "Darasimi", "08101431654")
# myCursor.execute(my_query, value)
# my_con.commit() # Automatically save it to the database
# print(myCursor.rowcount, "Record inserted")
# # my_con.cursor()
# print("Done")

for i in range(3):
    fullname = input("Your full name: ")
    Address = input("Your address: ")
    phone = input("Your phone number: ")
    pass_word = input("Your password: ")
    my_query = "INSERT INTO Registration_Table (address, password, full_name, phone_num) VALUES(%s, %s, %s, %s)"
    val = (Address, pass_word, fullname, phone)
    myCursor.execute(my_query, val)
    my_con.commit()
    print(myCursor.rowcount, "Record inserted")