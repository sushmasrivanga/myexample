

n1 = int(input())
n2 = input().split(" ")
res = []
print(n2)
for i in n2:
    if int(i)%2 == 0:
        res.append(i)

for i in n2:
    if int(i)%2 == 1:
        res.append(i)

print(" ".join(res))



