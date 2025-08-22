# from To_do_list_app import main as ad
import os
import pymysql as pyms
from dotenv import load_dotenv
load_dotenv()

dbPass = os.getenv("DB_PASS")

my_con = pyms.connect(host = '127.0.0.1', user = 'root', password = dbPass, db = "Todo_List")
# print("Connection Successful")

my_cursor = my_con.cursor()

# Creating a database for the app
# my_cursor.execute("CREATE DATABASE Todo_List")
# print("Successfully created!")

# Creating a table
# my_cursor.execute("CREATE TABLE To_do_list_table (task_id INT(4), task VARCHAR(100))")
# print("Table created")

# query = "ALTER TABLE To_do_list_table CHANGE task_id Task_id INT(5) PRIMARY KEY AUTO_INCREMENT"
# my_cursor.execute(query)

# my_query = "ALTER TABLE To_do_list_table ADD task_done VARCHAR(100)"
# my_cursor.execute(my_query)

# To print what's in column task
# my_cursor.execute("SELECT * FROM To_do_list_table")
# rows = my_cursor.fetchall()
# for row in my_cursor:
#     print(row)
# my_cursor.close()



# def get_db():
    # return my_con, my_cursor