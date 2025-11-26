
import sqlite3 
connect = sqlite3.connect('data_base_file.db')
cursor = connect.curser()

cursor.execute('creat table soldiers')

connect.commit()
connect.close()