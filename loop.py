# s = int(input("Enter a number: "))
# while s < 111:
#     print("suiiiii")
#     s = s + 12

# pasword = input("enter your password: ")    
# while pasword == "1234":
#     print("wrong password, try again")
#     if pasword == "12345":
#         break

# name = "savo"
# while True:
#     name_input = input("enter your name: ")
#     if name_input == name:
#         print("welcome")
#         break
#     else:
#         print("try again")        

# while True:
#     print("Who are you?")
#     name = input("Enter your name: ")
#     if name != "savo":
#         continue
#     print("Hello, Savo. What is the password? (It is a fish.)")
#     password = input("Enter password: ")
#     if password == "sardine":
#         print("access granted")
#         break

# print("hello")
# for i in range(5):
#     print("no i is set to: ", i)
# print("goodbye")    

# print('Hello!')
# i = 0
# while i < 5:
#     print('On this iteration, i is set to ' + str(i))
#     i = i + 1
# print('Goodbye!')

# import random
# for i in range(5):
#     print(random.randint(1, 10))


#guessing game
# import random
# number = random.randint(1, 20)
# print("I am thinking of a number between 1 and 20.")
# for i in range(6):
#     print("take a guess")
#     guess = int(input(">"))
#     if guess < number:
#         print("your guess is too low")
#     elif guess > number:
#         print("your guess is too high")
#     else:
#         break
# if guess == number:
#     print("good job! you guessed my number in " + str(i + 1) + " guesses!")
# else:
#     print("sorry, the number I was thinking of was " + str(number))


import random
wines = 0
losses = 0
ties = 0

while True:
    print('%s Wins, %s Losses, %s Ties' % (wines, losses, ties))
    print('Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit')
    player_move = input('>')
    if player_move == 'q':
        break
    if player_move != 'r' and player_move != 'p' and player_move != 's':
        print('Type one of r, p, s, or q.')
        continue

    if player_move == 'r':
        print('ROCK versus...')
    elif player_move == 'p':
        print('PAPER versus...')
    elif player_move == 's':
        print('SCISSORS versus...')

    random_number = random.randint(1, 3)
    if random_number == 1:
        computer_move = 'r'
        print('ROCK')
    elif random_number == 2:
        computer_move = 'p'
        print('PAPER')
    elif random_number == 3:
        computer_move = 's'
        print('SCISSORS')

    if player_move == computer_move:
        print('It is a tie!')
        ties = ties + 1
    elif (player_move == 'r' and computer_move == 's') or (player_move == 'p' and computer_move == 'r') or (player_move == 's' and computer_move == 'p'):
        print('You win!')
        wines = wines + 1
    else:
        print('You lose!')
        losses = losses + 1

    