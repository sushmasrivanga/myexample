n=int(input())
if(n<=0):
    print("Invalid Input")
    exit()
else:
    l=input()
    x=l.split(" ")
    o=[]
    e=[]
    f=[]
    fl=[]
    for i in range(0,n):
        fl.append(int(x[i]))
    fl.sort()
    for i in range(0,n):
        if(fl[i]%2==0):
            e.append(fl[i])
        else:
            o.append(fl[i])
f=e+o
for i in range(n):
    print(f[i],end=" ")
