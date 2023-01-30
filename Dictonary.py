'''

#write a program to combine list to a dictonary to form a hash table
#input :   keys=['name','age','branch']
#           vlaues=['abc','100','aeronautical']


keys=['Name','Age','Branch']
values=['sushma','20','CSE']
outsource=zip(keys,values)
abc=dict(outsource)
print(abc)

'''



'''
#write a program to store a sparse matrix into
#a dictonary
#example : [[0,0,0,1,0],
#           [2,0,0,0,4],
#           [0,0,0,4,0]]

matrix=[[0,0,0,1,0],
        [2,0,0,0,4],
        [0,0,0,4,0]]
print(len(matrix))
Dict={}
for i in range(len(matrix)):
    print("\n")
    for j in range(len(matrix[i])):
        print(matrix[i][j],end=' ')
        if matrix[i][j]!=0:
            Dict[i,j]=matrix[i][j]
print(Dict)
'''

'''

#program a non-repeated character in a string
#example : i/p - 1. 'level'
#          o/p - 2.  v

a='level'
for i in a:
    count=0
    for j in a:
        if i==j:
            count+=1
        if count>1:
            break
    if count==1:
        print("the non repeated char is ",i)

'''

'''
class Node:
    def __init__(self,num):
        self.num=num
        self.next=None
class llist:
    def __init__(self):
        self.head=None
    def push(self,newnum):
        newnode=Node(newnum)
        newnode.next=self.head
        self.head=newnode
    def insertnext(self,prenode,newnode):
        if prenode is None:
            print("the previous node")
            return
        newnode=Node(newnum)
        newnode.next=prenode.next
        prenode.next=newnode
    def append(self, newnum):
        newnode=Node(newnum)
        if self.head is None:
            self.head=newnode
            return
        last=self.head
        while(last.next):
            last=last.next
        last.next=newnode
    def printnum(self):
        t=self.head
        while(t):
            print(t.data)
            t=temp.next
if __name__=='__main__':
    ll=llist() 
    ll.append(1)
    ll.append(3)
    ll.append(5)
    ll.append(8)
    print(printnum)

'''













