print("Here in this game 'Snake water gun\n")
print("Here 0-snake , 1- water, 2 gun")

computer = int(input("Enter the your choice: "))
print("Computer choice is: ",computer)

player = int(input("Enter the player choice: "))
print("Player choice is: ",player)

if(computer == player):
    print("Game is draw")
elif(computer == 1 and player==0):
    print("Player win")
elif(computer == 0 and player==2):
    print("Player win")
elif(computer == 2 and player==1):
    print("Player win")
elif(computer == 2 and player==0):
    print("Computer win")
elif(computer==1 and player==2):
    print("Computer win")
elif(computer == 0 and player ==1):
    print("Computer win") 
else:
    print("Input value is wrong,choose the correct one")   

