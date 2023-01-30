'''
numListStr = input()

numStrArr = numListStr.split(",")
print(numStrArr)
print(numStrArr[::-1])
nums = []
for i in numStrArr:
    nums.append(int(i))

print(nums)

print(nums[::-1])

'''

def swap(l):
    n=len(l)
    temp=l[n-1]
    l[n-1]=l[0]
    l[0]=temp
    return 1
list=input()
mylist=list.split(",")
print(swap(list))
