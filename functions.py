# def deljenje(a, b):
#     return a / b
# x = deljenje(10, 2)
# print(x)

# print("sup", end=" ")
# print("bro")

# def a():
#     print("a go")
#     b()
#     d()
#     print("a stop")
# def b():
#     print("b go")
#     c()
#     print("b stop")
# def c():
#     print("c go")
#     print("c stop")
# def d():
#     print("d go")
#     print("d stop")
# a()


# def spam():
#     eggs = 'spam local'
#     print(eggs)  

# def bacon():
#     eggs = 'bacon local'
#     print(eggs)  
#     spam()
#     print(eggs)  
#     eggs = 'global'

# bacon()
# print(eggs)  


# def auto():
#     global x
#     x = "spam"

# x = 'global'
# auto()
# print(x)


# import time, sys
# indent = 0  # How many spaces to indent
# indent_increasing = True  # Whether the indentation is increasing or not

# try:
#     while True:  # The main program loop
#         print(' ' * indent, end='')
#         print('********')
#         time.sleep(0.1) # Pause for 1/10th of a second.

#         if indent_increasing:
#             # Increase the number of spaces:
#             indent = indent + 1
#             if indent == 20:
#                 # Change direction:
#                 indent_increasing = False
#         else:
#             # Decrease the number of spaces:
#             indent = indent - 1
#             if indent == 0:
#                 # Change direction:
#                 indent_increasing = True
# except KeyboardInterrupt:
#     sys.exit()


import time, sys  
try:
        while True:
            for i in range(1, 9):  
                print("-"*(i * i))  # skace probj - po kvadratu kada raste i koje je definisan gore
                time.sleep(0.1)

            for i in range(7, 0 , -1): # -1 je koliko se smanjuje, 7 pocetak i ide do 0, ali ne ukljucujuci 0
                                        #zato sto ne treba da ode u nule jer krece od keca u 1,9
                print("-"*(i * i)) # ista spika ali samo vezana za smajivanje
                time.sleep(0.1)

except KeyboardInterrupt:
    sys.exit()

