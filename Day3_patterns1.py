''' word="califonia"
x=""
for i in word:
    x+=i
    print(x)

w="india"
y=""
for i in w:
    y=y+i
    print(y)   '''

a=39
r=11
for i in range(0,r):
    for j in range(0,i+1):
        ch=chr(a)
        print(ch,end=" ")
        a+=1
    print(" ")


'''
a=65
r=11
for i in range(0,r):
    for j in range(0,i+1):
        ch=chr(a)
        print(ch,end=" ")
        a+=1
    print(" ")


a=65
r=6
m=(2*a)-2
for i in range(0,r):
    for j in range(0,m):
        print(end=" ")
    m=m-1
    for j in range(0,i+1):
        ch=chr(a)
        print(ch,end=" ")
        a+=1
    print(" ")   '''


''' n=10
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i*j,end=" ")
    print()  '''




n=5
for i in range(0,n+1):
    for j in range(0,i+1):
        print(i+j,end=" ")
    print()






