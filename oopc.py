'''
class Student:
    name="sushma"
    __rollno=34        #private variable is indicated by '__'(double underscore)

    def get_rollno(self):   #inorder to access private variable
        return self.__rollno
    def set_rollno(self,new_value):
        return self.__rollno=new_value
obj=Student()
print(obj.name)
print(obj.rollno)

'''

#inheritence

class A:
    def method_1(self):
        print("in class A")

class B:
    def method_1(self):
        print("in class B")

class Child(A,B):
    pass
obj=Child()
