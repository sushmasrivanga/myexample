'''
n=int(input())
#d={}
arr=[]
for i in range(n):
    name=input("enter your name: ")
    pw=int(input("enter your password: "))
    arr.append({name:pw})
    #d.update({name:pw})
print(arr)

'''


n=int(input())
arr=[]
for i in range(n):
    name=input("enter your name: ")
    pw=int(input("enter your password: "))
    arr.append({name:pw})
print(arr)
username=input("enter username to check: ")
password=int(input("enter your password: "))
found=False
for obj in arr:
    try:
        if(username==name and password==pw):
            print("valid username")
        else:
            print("invalid username")
    except:
        pass
if found==False:
    print("user not found")
