# INSIDE the function — raise the error
# def box_print(symbol, width, height):
#     if width <= 2:
#         raise Exception('Width must be greater than 2.')

# # OUTSIDE the function — catch and handle it
# try:
#     box_print('*', 1, 4)   # bad width, will raise
# except Exception as err:
#     print('An exception happened: ' + str(err))
    


# x = int(input("enter 1,2 or any other number: "))

# assert x > 1, "x must be greater than 1"
# print("x is greater than 1")

# print(factorial(5))
# logging.debug('End of program')


# import logging
# logging.basicConfig(level=logging.ERROR, format='%(asctime)s -  %(levelname)s -  %(message)s')

# def divide(a, b):
#     if b == 0:
#         logging.critical('Tried to divide by zero')
#         return None
    
#     if a<0 or b<0:
#         logging.error('Tried to divide by a negative number')
#     logging.debug(f'deviding {a} by {b}')
#     return a / b

# result = divide(10, 0)
# print(result)
