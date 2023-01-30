a='H'
print(ord(a))
b='e'
print(ord(b))
c='L'
print(ord(c))

n='HeLlo'
sum=0
mylist=str(n)
for i in mylist:
    #print(i,"-",ord(i))
    sum=sum+ord(i)
print(sum)
