import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

connection = MySQLdb.connect(
    host = 'localhost',
    port = 3306,
    user = 'mssimano',
    passwd = 'oleMissS26',
    db = 'mssimano'
)

cursor = connection.cursor()

# 4. Execute and fetch a query 
# !!when using variables, pass as %s and a tuple
cursor.execute("SELECT * FROM Users")
results = cursor.fetchall()
for row in results:
    print(row)

# Close 
cursor.close()
connection.close()


