'''
n=int(input("enter a number: "))
flag=False
if(n<0):
    print("Invalid Input")
else:
    for i in range(2,n):
        if i%2==0:
            flag=True
            break
if flag:
    print("True")
else:
    print("False")

'''


a=[1,2,3,4,5]
print(a,end=" ")

'''
    if a%2==0:
        print("even")
    else:
        print("odd")
'''
