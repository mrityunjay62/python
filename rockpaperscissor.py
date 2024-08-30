import random

user_choice=int(input("enter ur choice (0 for rock , 1 for paper and 2 for scissor)"))
computer_choice=random.randint(0,2)
print("computer_choice:")
print(computer_choice)

if user_choice==0 and computer_choice==2:
    print("you win")
elif user_choice==2 and computer_choice==0:
    print("you lose")
elif user_choice == computer_choice:
    print("match draw")
elif user_choice > computer_choice:
    print("you win")
elif user_choice < computer_choice:
    print("you lose")