


str="india"
index=0
while index<len(str):
    letter=str[index]
    print(chr(ord(letter)+2),end=' ')
    index+=1


"""#list=[0,0,7,6,14,12,21,18]
n=int(input("enter the position:"))
a=b=0
for i in range(1,n+1):
    if(i%2!=0):
        a=a+7
    else:
        b=b+6
if n%2!=0:
    print('{} at accordance {}'.format(n,a-7))
else:
    print('{} at accordance {}'.format(n,b-6))


n=int(input("enter the position: "))
if(n%2==0):
    n=n//2
    print(3**(n-1))
else:
    n=n//2+1
    print()"""

'''

#  1,1,2,3,4,9,8,27,16,81,32,243,64,729,128,2187
n=int(input("enter the position:"))
a=b=1
for i in range(0,n-1):
    if(i%2!=1):
        a=a*2
    else:
        b=b*3
if n%2!=0:
    print('{} at accordance {}'.format(n,a))
else:
    print('{} at accordance {}'.format(n,b))


'''

"""Andy wants to go on a vacation to de-stress himself.Therefore, he decides to take a
trip to island.If is given that he has many consicutive """
