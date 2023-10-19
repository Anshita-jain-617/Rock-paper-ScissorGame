import random


#function
def play_game():

    #user input choice by user
    user_choice=input("enter your choice (stone/paper/scissor) : ").lower()
    
    #randomly choose by device
    computer_choice=random.choice(["stone","paper","scissor"])

    print(f"users choice is {user_choice}")
    print(f"computers choice is {computer_choice}")

    # conditions
    if user_choice  ==  computer_choice:
        print("It's a tie")
    
    elif (user_choice=="rock" and computer_choice=="scissor") or (user_choice=="paper" and computer_choice=="rock") or (user_choice=="scissor" and computer_choice=="paper"):
        print("You Win !")
    
    else:
        print("Computer win !")
# Wanna play again?
while True:
    play_game()
    print("Do You Want to play again? yes/no? : ")

    play_again = input("enter yes if you want to play : ").lower()

    if play_again != "yes":
        break

print("Thank you for playing!")

