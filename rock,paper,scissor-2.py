from random import randint


choice = ['rock','paper','scissor']
player=input("choose from ['rock','paper','scissor']").lower()
comp=choice[randint(0,2)]
print(comp)

if player==comp:
    print("DRAW MATCH")
elif player=="paper" and comp=="rock":
    print("player1 wins")
    
elif player=="rock" and comp=="scissor":
    print("player1 wins")
    
elif player=="scissor" and comp=="paper":
    print("player1 wins")
    
else:
    print("computer won")



#print(random.randit(1,10))
