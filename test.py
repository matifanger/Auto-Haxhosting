import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

# Test de guardado de logs en Database

try:
    connection = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='haxserver')

    mySql_insert_query = """INSERT INTO hfs_console (csl_date, csl_type, csl_text) 
                           VALUES 
                           (%s, %s, %s) """

    entry = ('20010', '11T', "123")

    cursor = connection.cursor()
    cursor.execute(mySql_insert_query, entry)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into table")
    cursor.close()

except mysql.connector.Error as error:
    print("Failed to insert record into Laptop table {}".format(error))

finally:
    if (connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")
