# function - space is allocated in the memory location
#function is into two parts
# 1. function header
# 2. function body

'''

def fun(x,y):
    return x+y
a=5
b=8
print(fun(a,b))



    
def fun(a,b):
    c=a+b
    print(c)
x=9
y=1
fun(x,y)



def num():
    for i in range(10):
        print(i)
num()



def add(a,b):
    c=a+b
    print(c)
def sub(a,b):
    c=a-b
    print(c)
def mul(a,b):
    c=a*b
    print(c)

a=5
b=5
add(a,b)
sub(a,b)
mul(a,b)

'''


'''

var1="hi"
def abc():
    global var1
    var1="goodmorning"
    print("in the function var1 is -",var1)
abc()
print("outside funtion is var2 is -",var1)
var1="verygood"
print("outside function after modify ",var1)


'''
'''
# program to demo access of var in inner and outer func

def out_fun():
    out_var=11
    def in_fun():
        inner_var=22
        print("inner variable:",inner_var)
    in_fun()
    print("outer variable:",out_var)
out_fun()




#writing a function and return its cubation format

def cube(a):
    return a*a*a
num=5
print("cube of a number: ",cube(num))



# write a program to understand a mismatch parameters

def abc(x):
    print("hii students"+"x",5)
abc(5)


def fun(i):
    print("blue",i)
fun(5+2*4)



# program to demo key args

def display(str, int_x, float_y):
    print("the string is -",str)
    print("the integer is -",int_x)
    print("the float is -",float_y)
display(float_y=543.286, str="hii", int_x=54)
'''

'''
    
def disp(name,age,salary):
    print("name is :",name)
    print("age is :",age)
    print("salary is :",salary)
a="sushma"
b=20
c=12345
disp(age=b,name=a,salary=c)
disp(a,b,c)
'''


'''
# 1. lambda function has no names
# 2. it can take n number of attributes
# 3. it can only return one value
# 4. lambda function cannot access global variable
# 5. cannot access var other than their parameters list
# 6. cannot contain multi parameters
# 7. It does not  have explict return stmts

addition = lambda x,y:x+y
print("sum : ",addition(10,20))


# program to find smaller number by using lambda

def small(a,b):
    if(a<b):
        return a
    else:
        return b
add=lambda x,y:x+y
diff=lambda x,y:x-y
print("smaller of two no. ",small(add(-3,-2),diff(-1,2)))



def increment(y):
    return (lambda x:x+1)(y)
a=100
print("a=",a)
print("a after incrementing")
b=increment(a)
print(b)


def fun(f,n):
    print(f(n))
twice = lambda x:x*2
fun(twice,4)




x=lambda : sum(range(1,11))
print(x())


def swap(a,b):
    a=a+b   # 8=3+5
    b=a-b   # 3=8-5
    a=a-b   # 5=8-3
    print("after swapping  x:",a,"and y:",b)
x=3
y=5
print("before swapping  x:",x ,"and y:",y)
swap(x,y)





# write a program to return the full name of a person where 1st variable

def name(f_name,l_name):
    s=' '
    n=f_name+s+l_name
    return n

print(name("sushma sri","vanga"))
'''
'''

def evenodd(x):
    if(x%2==0):
        print(x,"is even number")
    else:
        print(x,"is odd number")

a=7
evenodd(a)
'''

'''

 write a program to calculate SI. suppose the customer is a senior citizen. He is begin
 offered 12% ROI; for all other customers, the ROI is 10%
p=200
r=3
si=p X r X ROI/100   


def sc(p,r):
    ROI=12/100
    res=(p*r*ROI)/100
    print(res)
def c(p,r):
    ROI=10/100
    res=(p*r*ROI)/100
    print(res)
p=200
r=3
sc(200,3)
c(200,3)



                                 # factorial using recursion

def fact(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*fact(n-1)
n=5
print(fact(n))



def exp(x,y):
     if y==0:
         return 1
     else:
         return(x*exp(x,y-1))

a=5
b=3
print("result",exp(a,b))

'''


'''
                    # fabinocci using function

def fib(x):
    a=0
    b=1
    for i in range(x):
        c=a+b
        print(i,"element",c)
        a=b
        b=c

n=10
fib(n)

                      # fabinocci using recursive function

def fibb(n):
    if n<2:
        return 1
    return (fibb(n-1)+fibb(n-2))
n=10
for i in range(n):
    print("Fabinocci (",i,")=",fibb(i))

'''


'''   
    
def hanoi(n,A,B,C):
    if n>0:
        hanoi(n-1,A,C,B)
        if A:
            C.append(A.pop())
        hanoi(n-1,B,A,C)
A=[1,2,3,4]
B=[]
C=[]
print(A,B,C)
hanoi(len(A),A,B,C)
print(A,B,C)



# check if two strings match where one string contains wildcard characters

def solve(a,b):
    n,m=len(a),len(b)
    if n==0 and m==0:
        return True
    if n>1 and a[0]=='*' and m==0:
        return False
    if(n>1 and a[0] =='?') or (n!=0 and m!=0 and a[0] ==b[0]):
        return solve(a[1:],b[1:])
    if n!=0 and a[0]=='*':
        return solve(a[1:],b) or solve(a,b[1:])
    return False
x=str(input("enter the string with char : "))
y=str(input("enter the string for match : "))
print("with wild characters :",x)
print("without wild characters ::",y)
print(solve(x,y))
'''




    












