# program to interviene polymorphism on a complex numbers
'''
class Complex():
    def __init__(self):
        self.real=0
        self.img=0
    def setvalue(self,real,img):
        self.real=real
        self.img=img
    def __add__(self,c):
        temp=complex()
        temp.real=self.real+c.real
        temp.img=self.img+c.img
        return temp
    def display(self):
        print("(",self.real,"+",self.img,"i)")
c1=Complex()
c1.setvalue(1,2)
c2=Complex()
c2.setvalue(3,4)
c3=c1+c2
print("result is..")
c3.display()

'''

# operator ------ function name-----
# +     __add__
# +=    __iadd__
# -     __sub__
# -=    __isub__
# *     __mul__
# *=    __imul__
# /     __truediv__
# /=    __idiv__
# **    __pow__
# **=   __ipow__
# %     __mod__
# %=    __imod__
# >>    __rshift__
# >>=   __irshift__
# <<    __lshift__
# <<=   __ilshift__
# &     __and__
# &=    __iand__
# |     __or__
# |=    __ior__
# ^     __xor__
# ^=    __ixor__
# ~     __invert__
# ~=    __iinvert__
# >     __gt__
# <     __lt__
# >=    __ge__
# <=    __le__




# program that has abstract class to derive 2 class
# rectangle and triangle from polygon class and
# write the methods to get their details and dimensions
# and hence calculate the area respectively
'''
class polygon:
    def get_data(self):
        raise NotImplementedError()
    def area(self):
        raise NotImplementedError()
class rectangle(polygon):
    def get_data(self):
        self.length=float(input("enter rectangle len"))
        self.breadth=float(input("enter rectangel breadth"))
    def area(self):
        return self.length * self.breadth

class triangle(polygon):
    def get_data(self):
        self.base=float(input("enter triangle base"))
        self.height=float(input("enter triangle height"))
    def area(self):
        return 0.5 * self.base * self.height
R=rectangle()
R.get_data()
print("area of a rectangle",R.area())
T=triangle()
T.get_data()
print("area of a triangle",T.area())
'''

'''
# ensapsulating public members
class pub:
    def __init__(self,name,num):
        self.name=name
        self.num=num
    def num(self):
        print("roll num is ",self.num)
obj=pub("hurry",299)
obj.num()

'''
'''
# program to overload the __call__method
class multi:
    def __init__(self,num):
        self.num=num
    def __call__(self,0):
        return self.num * 0
x=multi(10)
print(x(5))
'''



'''


# program to over-ride get-item and set-item methods

class mylist:
    def __init__(self,list):
        self.list=list
    def __getitem__(self,index):
        return self.list[index]
    def __setitem__(self,index,num):
        self.list[index]=num
    def __len__(self):
        return len(self.list)
    def display(self):
        print(self.list)
L=mylist([1,2,3,4,5,6,7,8,9])
print("list is.....")
L.display()
index=int(input("enter the index of the list"))
print(L[index])
num=int(input("enter the position u want to modify"))
L[index]=num
L.display()
print("the length of list is",len(L))

'''

'''
# special or miscellaneous functions in overloading

class number:
    def __init__(self,num):
        self.num=num
    def display(self):
        return self.num
    def __abs__(self):
        return abs(self.num)
    def __float__(self):
        return float(self.num)
    def __hex__(self):
        return hex(self.num)
    def __oct__(self):
        return oct(self.num)
    def __setitem__(self,num):
        self.num=num

n=number(-14)
print(" n is =",n.display())
print(" abs(n) is = ",abs(n))
n=abs(n)
print("converting to float",float(n))
print("converting to hexa",hex(n))
print("converting to octa",oct(n))

'''

'''
# to visualize inheritance flow

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("name is",self.name)
        print("age is",self.age)
class teacher(person):
    def __init__(self,name,age,exp,rarea):
        person.__init__(self,name,age)
        self.exp=exp
        self.rarea=rarea

    def displaydata(self):
        person.display(self)
        print("experience is ",self.exp)
        print("research area is ",self.rarea)
class student(person):
    def __init__(self,name,age,course,marks):
        person.__init__(self,name,age)
        self.course=course
        self.marks=marks
    def displaydata(self):
        person.display(self)
        print("course=",self.course)
        print("marks=",self.marks)
print("---------teacher class---------")
T=teacher("mark",43,20,"JSS")
T.displaydata()
print("---------student class---------")
S=student("sophie",20,"B.E",53)
S.displaydata()

print("T is a teacher: ",isinstance(T,teacher))

'''


'''
# program to invoke __init__in multiple inheritence

class base1(object):
    def __init__(self):
        print("base class 1")
class base2(object):
    def __init__(self):
        print("base class 2")
class Derived(base1,base2):
    pass
D=Derived()
'''

'''

class base1(object):
    def __init__(self):
        print("base class 1")
        super(base1,self).__init__()
class base2(object):
    def __init__(self):
        print("base class 2")
class Derived(base1,base2):
    pass
D=Derived()

'''

'''
class base1(object):
    def __init__(self):
        print("base class 1")
        super(base1,self).__init__()
class base2(object):
    def __init__(self):
        print("base class 2")
class Derived(base1,base2):
    def __init__(self):
        super(Derived,self).__init__()
        print("Derived class")
D=Derived()        

'''

'''
class person:
    def name(self):
        print("name is ...")
class teacher(person):
    def qual(self):
        print("qualification is phd")
class hod(teacher):
    def expe(self):
        print("experience is 22 yrs")
HOD=hod()
HOD.name()
HOD.qual()
HOD.expe()

'''

# multi path inheritence

class student:
    def name(self):
        print("name...")
class academic(student):
    def acad_score(self):
        print("academic score 90% above")
class EEE(student):
    def EEE_score(self):
        print("EEE score---- 60% and above")
class result(academic):
    def eligibility(self):
        print("_______eligibility to apply_______")
        self.acad_score()
        self.EEE_score()
R=result()
R.eligibility()




