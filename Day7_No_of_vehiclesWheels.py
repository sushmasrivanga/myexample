v=int(input())
w=int(input())
if w&1==1 or w<2 or w<=v:
    print("invalid input")
else:
    x=((4*v)-w)//2
print(" tw ",x)
print("fw",v-x)



