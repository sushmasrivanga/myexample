'''def fun():
    print("hii")
fun()


def sub(a,b):
    return a-b

x=5
y=3
result=sub
print(result(x,y))  '''


'''   To speed up his composition of generating unpredictable rhythms, blue  bandit wants
the list of prime numbers available in a range of numbers. can you help him out?
write a java/python/c++ program to print all prime numbers in the interval [a,b] (a and b,
both inclusive).
NOTE:
    input 1 should be lesser than input 2.both the inputs should be positive.
Range must always be greater than zero.
if any one of the condition fails display "provide valid input"
use min of one for loop and one while loop

sample i/p 1:
    2
    15
sample o/p 1:
    2 3 5 7 11 13      '''


'''
x=int(input("enter start number:"))
y=int(input("enter end number:"))
if(a<=0 or b<=0 or a>b):
    print("provide valid input")
else:
    while(x<=y):
        if(x==2):
            print()
        elif(x==1):
            x+=1
            continue
        else:
            flag=0
            for i in range(2,x//2+1):
                if x%i==0:
                    flag=1
                    break
            if flag==0:
                print(x,end=" ")
        x+=1
'''






'''
# x - pattern
n=5
val=n*2-1
for i in range(1,val+1):
    for j in range(1,val+1):
        if i==j or j==val-i +1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("\n")



# plus - pattern
n=5
val=n*2-1
for i in range(1,2*n):
    for j in range(1,2*n):
        if i==n or j==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("\n")
'''

n=11
val=0
st=int(n/2+1)
if n%2!=0:
    for i in range(1,int(n/2+2)):
        for j in range(1,val+1):
            print(' ',end=" ")
        for k in range(1,st+1):
            print('*',end=' ')
        print()
        val+=1
        st-=1
    val-=2
    st+=2
    for i in range(int(n/2+2),n+1):
        for j in range(1,val+1):
            print(' ',end=" ")
        for k in range(1,st+1):
            print('*',end=" ")
        print()
        val-=1
        st+=1
else:
    print("provide accurate input")
    

