# pip install pymysql

import pymysql as pyms

my_con = pyms.connect(host = '127.0.0.1', user = 'root', password = 'Musty@@@@@12345')
print('Connection Successful')