import random
game_number=random.randint(1,100)
print(game_number)
while True:
    guess= int(input("Enter A Number: "))
    if game_number<guess:
        print("Too high!")
    elif game_number>guess:
        print("Too low")
    else:
         print("winner winner chicken dinner")