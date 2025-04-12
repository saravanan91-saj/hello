#class
"""
class myclass:
    def function(self):
        print("hello world")
obj=myclass()
obj.function()
"""
#Class using variable
"""
class mynum:
    a=10
    def num1(self):
        print("Hello")
obj=mynum()
obj.num1()
print(obj.a)
"""
#Class
"""
class mynum:
    a=15
    def num(self):
        print("self")
obj=mynum()
obj.num()
value=obj.a
print(value)
"""
"""
class num:
    a=10
    def num1(self,a,b):
        self.a=a
        self.b=b
        print("self")
    def num2(self):
        c=self.a+self.b
        print("Sum:",c)
obj=num()
obj.num1(15,20)
obj.num2()
value=obj.a
print("val:",value)
"""
"""
class student:
    def data(self,name,age,dept,contact_no):
        print("Name:",name)
        print("Age:",age)
        print("Dept:",dept)
        print("Contact No:",contact_no)
obj=student()
obj.data("Saran",30,"IT",8438206091)
"""
"""
class student:
    def data(self,name,age,dept,contact_no):
        self.name=name
        print("Name:",name)
        print("Age:",age)
        print("Dept:",dept)
        print("Contact_no:",contact_no)
    def data1(self):
        print("Welcom:",self.name)
obj=student()
obj.data("Saran",30,"IT",8438206091)
obj.data1()
"""
#Inheritance
"""
class student:
    def data1(self):
        print("Saran is top scorer")
class student1(student):
    def data2(self):
        print("Vino is least scorer")
s1=student1()
s1.data1()
s1.data2()
"""
#1. single inheritance
"""
class Addition:
    def add(self):
        a=int(input("Enter a value:"))
        b=int(input("Enter b value:"))
        c=a+b
        print("Value:",c)
class Subraction(Addition):
    def sub(self):
        a=int(input("Enter a value:"))
        b=int(input("Enter b value:"))
        c=a-b
        print("Value:",c)
obj=Subraction()
obj.add()
obj.sub()
"""
#2.Multiple inheritance
"""
class Addition:
    def mult(self):
        a=int(input("Enter a value:"))
        b=int(input("Enter b value:"))
        self.a=a
        self.b=b
        c=a*b
        print(c)
class subract:
    def div(self):
        c=self.a/self.b
        print(c)
class Result(Addition,subract):
    def res(self):
        self.mult()
        self.div()
obj=Result()
obj.res()
"""
#3.Multilevel inheritance
"""
class Biodata:
    def student(self,name,age):
        self.name=name
        self.age=age
        print("Student Name:",name)
        print("Age",age)
        print(f"Student Name is {name} , I am {age}")
class data(Biodata):
    def employee(self):
        print("employee Name:",self.name)
        print("employee age:",self.age)
class input(data):
    def res(self):
        self.student("saran",36)
        self.employee()
obj=input()
obj.res()
"""
#4.Hierarchical inheritance
"""
class get:
    def getin(self):
        self.a=int(input("enter a value:"))
        self.b=int(input("enter b value:"))
class addition(get):
    def add(self):
        self.getin()
        c=self.a+self.b
        print(c)
class subract(get):
    def sub(self):
        self.getin()
        c=self.a-self.b
        print(c)
obj1=addition()
obj1.add()
obj2=subract()
obj2.sub()
"""    
#Hybrid inheritance
"""
class get:
    def value(self):
        self.name=input("Enter name:")
class student(get):
    def stu(self):
        self.value()
        studId=input("Enter StudentId:")
        print(f"Student name:{self.name},Student Id:{studId}")
class employee(get):
    def emp(self):
        self.value()
        empId=input("Enter Employee ID:")
        print(f"Employee name:{self.name},Emp Id:{empId}")
class input1(student,employee):
    def inp(self):
        self.stu()
        self.emp()
obj=input1()
obj.inp()
"""
#polymorphism
"""
class student:
    def stud(self):
        print("Senior Student")
class tenth(student):
    def stud(self):
        print("10th standard student")
class ninth(student):
    def stud(self):
        print("9th standard student")
class fifth(student):
    def stud(self):
        print("Junior Student")
s1=student()
s1.stud()
s2=tenth()
s2.stud()
s3=ninth()
s3.stud()
s4=fifth()
s4.stud()
"""
#constructor
class student:
    def __init__(self,name):
        print("Welcome:",name)
obj=student("Saran")

    



        
