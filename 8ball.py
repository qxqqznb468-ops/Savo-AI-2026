# import random
# messages = ['It is certain',
#     'It is decidedly so',
#     'Yes definitely',
#     'Reply hazy try again',
#     'Ask again later',
#     'Concentrate and ask again',
#     'My reply is no',
#     'Outlook not so good',
#     'Very doubtful']
# print('Ask a yes or no question:')
# input('')
# print(messages[random.randint(0, len(messages) - 1)])


import random, sys, time

WIDTH = 70  # The number of columns

try:
    columns = [0] * WIDTH
    while True:
     
        for i in range(WIDTH):
            if random.random() < 0.02:

                columns[i] = random.randint(4, 14)

            if columns[i] == 0:

                print(' ', end='')
            else:
                print(random.choice([0, 1]), end='')
                columns[i] -= 1  
        print()  
        time.sleep(0.1)  
except KeyboardInterrupt:
    sys.exit()  