#n=int(input())
#for i in range(n):
#    l=int(input())

a = input()
n = input().split(" ")[:int(a)]
res = 1

for i in n:
    res = res * int(i)

print(res)
