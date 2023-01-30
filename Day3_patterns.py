'''str1="ABCDEFGH"
str2="ate"
for letter in str1:
    print(letter +str2,end=" ")'''



'''   patterns:-
     1. Basic patterns
     2.mirror image patterns
     3.symmetrical patterns
     4.choice of patterns    -   cross, horizontal
     5.anti-pattern / hallow patterns    '''



'''  

n=5
for i in range(n):
    for j in range(i+1):
        print(j+1,end=" ")
    print("\n")



n=5
for i in range(n,0,-1):
    for j in range(0,i):
        print(j+1,end=" ")
    print("\n")   



n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if(j>i):
            print("*", end=" ")
    print('\n')





n=5
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print("\n")
'''

  
n=5
for i in range(n,0,-1):
    for j in range(0,i):
        print("*",end=" ")
    print("\n")

n=5
for i in range(n,0,-1):
    for j in range(1,n+1):
        if(i>j):
            print(' ',end=" ")
        else:
            print("*",end=" ")
    print("\n")

n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if(j<i):
            print(' ',end=" ")
        else:
            print("*",end=" ")
    print("\n")   


''' n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if(j<i):
            print("",end=" ")
        else:
            print("*",end=" ")
    print()  '''




'''   rows=int(input("enter no. of rows: "))
i=1
while i<=rows:
    j=rows
    while j>i:
        print(' ',end=' ')
        j-=1
    print('*',end=' ')
    k=1
    while k<2 *(i-1):
        print(' ',end=' ')
        k+=1
    if i==1:
        print()
    else:
        print('*')
    i+=1
i=rows-1
while i>=1:
    j=rows
    while j>i:
        print(' ',end=" ")
        j-=1
    print('*',end=" ")
    k=1
    while k<2 *(i-1):
        print(' ',end=" ")
        k+=1
    if i==1:
        print()
    else:
        print('*')
    i-=1    '''
        




rows=5
k=2*rows-2
for i in range(0,rows):
    for j in range(0,k):
        print(end=" ")
    k=k-1
    for j in range(0,i+1):
        print("*",end=" ")
    print(" ")
k=rows-2
for i in range(rows,-1,-1):
    for j in range(k,0,-1):
        print(end=" ")
    k=k+1
    for j in range(0,i+1):
        print("*",end=" ")
    print("")
        







''' n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if(j>i):
            print('*',end=" ")
        else:
            print('',end=" ")
    print("\n") '''



