import random
print("lets play rock, paper, scisor")
start=input("rock,paper,scissor")
user_input=["rock","paper","scissor"]
computor_choice=(random.choice(user_input))

print("You chose:",start )
print("Computer chose:", computor_choice)

if start==computor_choice:
    print("draw ")
elif start =="rock":   
    if computor_choice=="paper": 
        print("paper wrapes rock you lose")
    else:
        print("rock smashes scissor you won")
elif start=="paper":   
    if computor_choice=="rock": 
        print("paper wrapes rock you won")
    else:
        print("scissor cut paper you lose")
elif start=="scissor":   
    if computor_choice=="paper": 
        print("scissor cut paper you won")
    else:
        print("rock smashes scissor you lose") 

else:
    print("invalid game")           

                           






