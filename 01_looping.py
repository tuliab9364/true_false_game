import random

how_many = 3
won = 0
lost = 0

game_history = []

print()
print("*****Welcome To True or False*****")
print()
print("Please type in true or false to answer the question")
print()
print("**** HAVE FUN!  *****")
print()

for item in range(1, how_many + 1):

    result = input("{} > {} ".format (1 , 100))
    

    if result == "won":
        feedback = "You won"
        won += 1
    else:
        feedback = "Sorry, you lost"
        lost += 1

    round_result = " Round {}: {}".format(item, feedback)
    game_history.append(round_result)
      
print()
print("***** Results *****")

for item in game_history:
    print(item)
