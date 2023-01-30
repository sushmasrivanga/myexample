
x=7 #int(input())
y=5 #int(input())
p=25 #int(input())
q=35 #int(input())
count=0
for i in range(p,q+1):
    if(i%x==0 and i%y==0):
        count+=1
print(count)
