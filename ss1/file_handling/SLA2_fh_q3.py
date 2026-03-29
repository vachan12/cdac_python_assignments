class Person:
    def __init__(self,pid=0,pname="",emailid="",mobno=""):
        self.__pid=pid
        self.__pname=pname
        self.__emailid=emailid
        self.__mobno=mobno

        def set_pid(self,pid):
            self.__pid=pid
        def get_pid(self):
            return self.__pid
        def set_pname(self,pname):
            self.__pname=pname
        def get_pname(self):
            return self.__pname
        def set_emailid(self,emailid):
            self.__emailid=emailid
        def get_emailid(self):
            return self.__emailid
        def set_mobno(self,mobno):
            self.__mobno=mobno
        def get_mobno(self):
            return self.__mobno
        
        def __str__(self):
            return f"Person[pid={self.__pid}, pname={self.__pname}, emailid={self.__emailid}, mobno={self.__mobno}]"
        
class Employee(Person):
    def __init__(self,pid=0,pname="",emailid="",mobno="",dept="",salary=0.0):
        super().__init__(pid,pname,emailid,mobno)
        self.__dept=dept
        self.__salary=salary

    def set_dept(self,dept):
        self.__dept=dept
    def get_dept(self):
        return self.__dept
    def set_salary(self,salary):
        self.__salary=salary
    def get_salary(self):
        return self.__salary
    def net_salary(self):
        Netsal = self.__salary + (self.__salary * 0.1)
        return Netsal

    def __str__(self):
        return super().__str__() + f", Employee[dept={self.__dept}, salary={self.__salary}]"
    
class Member(Person):
    def __init__(self,pid=0,pname="",emailid="",mobno="",memtype="",amtPaid=0.0):
        super().__init__(pid,pname,emailid,mobno)
        self.__memtype=memtype
        self.__amtPaid=amtPaid
    def set_memtype(self,memtype):
        self.__memtype=memtype
    def get_memtype(self):
        return self.__memtype
    def set_amtPaid(self,amtPaid):
        self.__amtPaid=amtPaid
    def get_amtPaid(self):
        return self.__amtPaid
    
    def __str__(self):
        return super().__str__() + f", Member[memtype={self.__memtype}, amtPaid={self.__amtPaid}]"
if __name__ == "__main__":
    emp1 = Employee(1, "John Doe", "john.doe@example.com", "1234567890", "IT", 50000.0)
    print(emp1)
    mem1 = Member(2, "Jane Smith", "jane.smith@example.com", "0987654321", "Gold", 1000.0)
    print(mem1)     
    person1 = Person(3, "Alice Brown", "alice.brown@example.com", "555-1234")
    print(person1)