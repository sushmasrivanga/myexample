'''

l=[12,34,23,56,34]
size=len(l)
temp=size-1
size-1=l[0]
l[0]=



# program to access a class var using a class object

class abc:
    var=22
    def disp(self):
        print("this is a class method")
obj=abc()
print(obj.var)
obj.disp()
'''

'''
# program to illustrate the constructor __init__() ....method

class abc:
    def __init__(self,var1,var2):
        print("in class method")
        self.var1,var2=var1,var2
        print("the value is:",var1)
        print("the value is:",var2)
obj=abc(10,20)
        


class abc():
    class_var=0
    def __init__(self,var):
        abc.class_var+=1
        self.var=var
        print("the obj var is",var)
        print("the class value of c-=var",abc.class_var)
obj1=abc(10)
obj2=abc(20)
obj3=abc(30)




class number:
    even=0
    def check(self,num):
        if num%2==0:
            self.even=1
    def even_odd(self,num):
        self.check(num)
        if self.even==1:
            print(num,"is even")
        else:
            print(num,"is odd")
obj=number()
obj.even_odd(22)



class number:
    evens=[]
    odds=[]
    def __init__(self,n):
        self.n=n
        if n%2==0:
            number.evens.append(n)
        else:
            number.odds.append(n)

n1=number(21)
n2=number(12)
n3=number(34)
n4=number(55)
n5=number(76)
print("even numbers; ",number.evens)
print("odd numbers: ",number.odds)



class abc():
    class_var=0
    def __init__(self,var):
        abc.class_var=+1
        self.var=var
        print("the object value is",var)
        print("the class value",abc.class_var)
    def __del__(self):
        abc.class_var-=1
        print("object with value %d is going out of scope",self.var)
obj1=abc(11)
obj2=abc(12)
obj3=abc(13)
del obj1
del obj2
del obj3

'''


'''

#  __repr__ ----- syntax report of the object
#  __cmp__ ------ compare two class objects
#  __len__  ---- len(object)
#  __call__  ---- it acts like a function to call its instances
#  __lt__, __le__, __eq__, __ne__, __gt__, __ge__ ---- to compare 2 objects
#  __iter__  ---- iteration over an object
#  __getitem__ used for indexing    gs : def __getitem__(self,var/key)

#  set item assign an item to the indexed value


# program to demonstrate get and set items in a list

class numbers:
    def __init__(self,mylist):
        self.mylist=mylist
    def __getitem__(self,index):
        return self.mylist[index]
    def __setitem__(self,index,val):
        self.mylist[index]=val
numlist=numbers([1,2,3,4,5,6,7,8,9])
print(numlist.mylist)
numlist[3]=10
print(numlist.mylist)



class ABC():
    def __init__(self,name,var):
        self.name=name
        self.var=var
    def __repr__(self):
        return repr(self.var)
    def __len__(self):
        return len(self.obj)
    def __cmp__(self):
        return self.var - obj.var
obj=ABC("abcdef",10)
print("the value stored in obj is",repr(obj))
print("the length of the name sorted in obj",len(obj))
obj1=ABC("ghijkl",1)
val=obj.__cmp__(obj1)
if val==0:
    print("both values are equal")
elif val==-1:
    print("1st values is less than second")
else:
    print("2nd value less than 1st")


# to call a class method from another method of same class

class abc():
    def __init__(self,var):
        self.var=var
    def display(self):
        print("var is =",self.var)
    def add_2(self):
        self.var+=2
        self.display()
obj= abc(10)
obj.add_2()  


# program to show how a class method calls a function which defined in the global name space

def scale_10(x):
    return x*10
class abc():
    def __init__(self,var):
        self.var=var
    def display(self):
        print("var is =",self.var)
    def modify(self):
        self.var=scale_10(self.var)

obj = abc(10)
obj.display()
obj.modify()
obj.display()

'''


'''
# built-in attributes for get set and delete
# 1. hasattr(obj, name)-checks obj possesses the attributes values or not
# 2. getattr(obj,name[,default])
# 3. setattr(obj, name, value)--
  #  which is used to set an atttribute of the obj
# 4. delattr(obj,name)



# program to demo builtin

class abc():
    def __init__(self,var):
        self.var=var
    def display(self):
        print("var is",self.var)
obj=abc(10)
obj.display()
print("check whether obj has attribute var ?",hasattr(obj,'var'))
getattr(obj,'var')
setattr(obj,'var',50)
print("after setting value, var is",obj.var)
setattr(obj,'count',10)
print("new variable count is created and its val=",obj.count)
delattr(obj,'var')
setattr(obj,'var',40)
print("after deleted the attr",obj.var)



# built in class attributes
# 1. .__dict__
# 2. .__doc__
# 3. .__name__    (name of the module in which the class is defined)
# 4. .__bases__


class abc():
    def __init__(self,var1,var2):
        self.var1=var1
        self.var2=var2
    def display(self):
        print("var1 is = ",self.var1)
        print("var2 is = ",self.var2)
obj=abc(10,12.34)
obj.display()
print("object.__dict__ - ",obj.__dict__)
print("object.__doc__ - ",obj.__doc__)
print("object.__name__ - ",abc.__name__)
print("object.__module__ - ",obj.__module__)
print("object.__bases__ - ",abc.__bases__)


'''



def swap(l):
    size=len(l)
    temp=l[0]
    l[0]=l[size-1]
    l[size-1]=temp
    return l


l=int(input())
print(swap(l))





'''

n=5
print(bin(n)[:2])


'''















