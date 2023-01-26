from pymysql import *
con = connect(host="localhost",user="root",password="",database="Employee_details")
cur = con.cursor()
class Employee:
    def __init__(self):
        q = "select * from emp_details;"
        cur.execute(q)
        det = cur.fetchall()
        print("Id\tName\tDept\tSalary")
        for i in det:
            for j in i:
                print(j,end="\t")
                
            print()
        print("*" * 50)
        print()
    def Add_employee(self,name,dept,salary):
        if (len(dept)<=7 and len(name)<=7):
            emp_name = name
            emp_dept_name = dept
        else:
            emp_name = name[:7]
            emp_dept_name = dept[:7]
        q = f"insert into emp_details(Name,Department_Name,Salary) values('{emp_name}','{emp_dept_name}',{salary})"
        cur.execute(q)
        con.commit()
        print("Data saved.....")
        print()
        print("*" * 50)
    def Update(self,ID):
        q = f" select * from emp_details where Id = {ID}"
        cur.execute(q)
        emp_det= cur.fetchall()
        print("Id\tName\tDepartment_Name\t\tSalary")
        
        for i in emp_det:
            for j in i:
                print(j,end="\t\t")
        print()
        opt = int(input("Which one do you want to change\n1.Employee Name\n2.Employee Department\n3.Employee Salary\nSelect any one option:"))
        if (opt == 1):
            n =input("Enter the Name :")
            q = f"update emp_details set Name = '{n}' where ID={ID}"
            cur.execute(q)
            con.commit()
            print("Name was updated....")
            
        elif (opt == 2):
            d =input("Enter the Department Name :")
            q = f"update emp_details set Department_Name = '{d}' where ID={ID}"
            cur.execute(q)
            con.commit()
           
            print("Department_Name was updated....")
        elif (opt == 3):
            s =input("Enter the Salary :")
            q = f"update emp_details set Salary = '{s}' where ID={ID}"
            cur.execute(q)
            con.commit()
            con.close()
            print("Salary was updated....")
        else:
            print("Invalid option...")
        print()
        print("*" * 50)
    def Delete(self,ID):
        q=f"Delete from emp_details where ID = {ID}"
        cur.execute(q)
        con.commit()
        print()
        print("Data Deleted Successfully.....")
        print()
        print("*" * 50)
    
while True:  
    Emp = Employee()
    opt = int(input("1.Add Employee Details\n2.Modify Employee Details\n3.Delete Employee Details\n4.Exit\n\nSelect any one Option :"))
    print()
    if ( opt == 1):
        emp_name = input("Enter the Employee Name :")
        emp_dept_name = input("Enter the Employee Department Name :")
        emp_salary = int(input("Enter the Employee Salary :"))
        
        Emp.Add_employee(emp_name,emp_dept_name,emp_salary)
    elif (opt == 2):
        ID = int(input("Enter the Employee Id do you want to modify:"))
        Emp.Update(ID)
    elif (opt == 3 ):
        ID=int(input("Enter the Employee ID do you want to Delete :"))
        Emp.Delete(ID)
    elif (opt == 4 ):
        print("Thank You....")
        break
    else:
        print("Please select the Valid option...")
        