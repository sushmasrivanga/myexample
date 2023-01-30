
'''

inpStr = input()
mylist=inpStr.split(",")
res=[]
res.append(int(mylist[-1]))
for i in mylist[1:-1]:
    res.append(int(i))

res.append(int(mylist[0]))

print(res)

'''

'''
inpStr = input()
mylist=inpStr.split(",")
n=len(mylist)
mylist[0],mylist[-1]=int(mylist[-1]),int(mylist[0])
print(mylist)
'''

'''
a=int(input())
b=int(input())
count=0
for i in range(a,b):
    if(i%7==0 and i%5==0):
        count=count+1
print(count)
'''

'''
a=input()
mylist=a.split(",")
print(mylist)
'''
'''
import array as arr

a=input()  #arr.array('i',[1,2,3,4,5,6])
n=3
#for i in range(0,6):
 #   print(a[i],end=" ")
#print()
new=a[:n]
new1=a[]
print(new)

'''

'''

l=[1,2,3,4,5,6]
index=2
n1=l[:index]
print(n1)
'''


'''
i=0
while i<=1:
    print(a[i],end=" ")
    i=i+1
print()

i=2
while i<=3:
    print(a[i],end=" ")
    i=i+1
print()

i=4
while i<=5:
    print(a[i],end=" ")
    i=i+1
print()
'''

'''
def swap(a,b,c):
    temp=a
    a=c
    c=temp
    return a,b,c

n=input()
print(n)
arr=n.split(",")
print(arr)
res=swap(arr[0],arr[1],arr[2])
print(list(res))
'''


l1=input()
l2=[]
n=len(l1)
for i in range(n):
    if(i==0):
        l2.append(l1[









