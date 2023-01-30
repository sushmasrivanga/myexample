
'''

n=123
rev=0
while(n>0):
    rem=n%10
    print(rem,end=" ")
    n=n//10
'''

# reversing list

'''
a=[1,2,3,4]
print(a)
reverse=a[::-1]
print(reverse)

b=[6,7,8,9]
print(b)
b.reverse()
print(b)

'''


'''
a=int(input())
print(a)
a.reverse()
print(a)

'''



def reverse(n):
    if len(n)==0:
        return n
    return reverse(n[1:]) + n[0]
num=1,2,3,4
n_string=str(num)
r_num=reverse(n_string)
print("reversed number is: "+r_num)


"""sum=0
avg=0.0
for i in range(1,11):
    print(i)
    sum=sum+i
print("addition of the numbers:",sum)
avg=sum/i
print(avg)"""




"""n=int(input("enter a number: "))
for i in range(1,11):
    print(n,"*",i,"=",n*i)"""


"""for i in range(1900,2101):
    if i%4==0:
        print(i,end=" ")"""


"""n=int(input("enter a number: "))
sum=0.0
for i in range(1,n+1):
    a=1.0/i
    sum=sum+a
print("the sum of 1,1/2....1/"+str(n)+"is"+str(sum))
    



num=int(input())
s=0.0
for i in range(1,num+1):
    a=1.0/i**2
    s=s+a
print("the sum of 1,1/2....1/"+str(num)+"is"+str(s))"""




str="hello"
print(str.center(10,'$'))


"""
str="ll"
substr="hehellhehell"
print(substr.count(str,0,len(substr)))


str="he is my cousin"
print(str.find("my",0,len(str)))

#left and right justification
str="hi"
print(str.ljust(10,'*'))

str="hi"
print(str.rjust(10,'*'))



#syntax for zfill(width)
str="5"
print(str.zfill(4))

#ASCII value
a="zebra"
print(max(a))
print(ord(max(a)))

"""

str="rose is a flower"
print(str.title())      # o/p - Rose Is A Flower
print(str.capitalize())  # o/p - Rose is a flower

str="Rose Is A Flower"
print(str.swapcase())
print(list(enumerate(str)))  # o/p - rOSE iS a fLOWER

'''

str="India has won"
for i in str:
    print(i,end=" ")


'''
