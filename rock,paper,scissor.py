from random import randint

# rock , paper , scissor game with limit

choice = ['rock','paper','scissor']
n=int(input("enter number of turns : "))
#limit=3
pc=0
cc=0
for i in range(n):
    player=input("choose from ['rock','paper','scissor']").lower()
    comp=choice[randint(0,2)]
    print(comp)
    if player==comp:
        print("DRAW MATCH")
    elif player=="paper" and comp=="rock":
        print("player1 wins")
        pc=pc+1
    elif player=="rock" and comp=="scissor":
        print("player1 wins")
        pc=pc+1
    elif player=="scissor" and comp=="paper":
        print("player1 wins")
        pc+=1
    else:
        print("computer won")
        cc=cc+1
    if pc == n or cc == n:
        break
print("player count is : "pc)
print("computer count is : "cc)
if pc > cc:
    print("player1 wins")
    
else:
    print("computer wins")

