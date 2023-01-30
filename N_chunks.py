'''

a=int(input())
n=input()
arr=n.split(" ")
print(arr)
size=int(input())
if a%2!=0:
    print("Invalid Input")
else:
    for i in range(0,a):
        if size==2:
            if(i<=1):
                print(arr[i],end=" ")
            elif(i<=3):
                print(arr[i],end=" ")
            else:
                print(arr[i],end=" ")
'''

'''
def split(l,s):
    for i in range(0,len(l),s):
        yield l[i:i + s]

a=int(input())  #6
b=input()
arr=b.split(" ")
c=int(input()) #2
print(split(b,c))

'''


'''

def split(list_a, chunk_size):

  for i in range(0, len(list_a), chunk_size):
    yield list_a[i:i + chunk_size]

chunk_size = 2
my_list = [1,2,3,4,5,6,7,8,9]
print(list(split(my_list, chunk_size)))

'''

a=int(input())
n=input()
arr=n.split(" ")
print(arr)
size=int(input())
if a%2!=0:
    print("Invalid Input")
else:
    for i in range(0,len(arr),size):
        print(" ".join(arr[i:i+size]))
        print()
