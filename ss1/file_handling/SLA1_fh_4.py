import pymysql
try:
    # Connect to the database
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        database='test_db'
    )
    print("Connection successful!")
    cursor = connection.cursor()
    
except Exception as e:
    print(f"Connection failed: {e}")
finally:
    connection.close()
    print("Connection closed.")