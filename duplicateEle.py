
n=input().split(" ")

if len(n) != len(set(n)):
    print("True")
else:
    print("False")