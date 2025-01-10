import random
playing=True
game=(random.randint(0,9))

while playing:
    play=int(input("the game is to guess the number between 0 to 9 and if it is same to the number of the computer you win"))
    if game==play:
        print("you won the game")
        print("the number was",game)
        break
    else:
        print("sorry you lost please try again")
        print("the number was",game)

