import pymysql

try:
    conn = pymysql.connect(host = 'localhost', port = 3306, user = 'root',
    passwd = 'bda123', db ='bda2026')
    
    if conn != None:
        print("connection done")
    
    else:
        print("connection failed")
except Exception as e:
    print(e)


def insertDept():
    deptno = int(input("Enter deptno: "))
    dname = input("Enter dept name: ")
    cur.execute("insert into dept values(%s, %s)", (deptno, dname))
    conn.commit()
    return True


def deletedept(dept_id):
    cur.execute("delete from dept where dept_id = %s", (dept_id,))
    return True

def updatedept(dept_id, dname):
    cur.execute("update dept set dname = %s where dep_id = %s", (dname, dept_id))
    return True

def displayall():
    cur.execute("select * from dept")
    for data in cur.fetchall():
        print(f"dept_id: {data[0]}, dept name: {data[1]}")
    
def displaydept(dept_id):
    cur.execute("select * from dept where dept_id = %s", (dept_id,))
    data = cur.fetchone()
    print(f"dept_id: {data[0]}, dept name: {data[1]}")


try:
    cur =  conn.cursor()    
    choice = 0 
    while choice !=6:
        choice  = int(input("""
        1. insert dept
        2. delete dept
        3. update dept
        4. display all
        5. dsiplay dept
        6. exit
        """))
        
        match choice:
            case 1:
                status = insertDept()
                if status: 
                    print("Value inserted")
                else:
                    print("not inserted")
            case 2:
                dept_id = int(input("Enter deptid: "))
                status = deletedept(dept_id)
                if status:
                    print("record deleted")
                else:
                    print("delete failed")
            case 3:
                dept_id = int(input("Enter deptid: "))
                dname = input("Enter name to update")
                status = updatedept(dept_id, dname)
                if status:
                    print("Record Updated")
                else:
                    print("Unable to update")
            case 4: 
               displayall()
            case 5:
                dept_id = int(input("Enter id: "))
                displaydept(dept_id)
            case _:
                print("invalid choice")
    else:
        print("fail")
except Exception as e:
    print(e)
finally:
    if conn!= None:
        cur.close()
        conn.close