#exercise 1
price1 = int(input("enter price of item 1: "))
price2 = int(input("enter price of item 2: "))  
price3 = int(input("enter price of item 3: "))  
subtotal = price1 + price2 + price3
print("subtotal: ", subtotal)
tax = subtotal * 0.085
total = subtotal - tax
print("tax:$", round(tax, 2))
print("total:$", round(total, 2))

#exercise 2

grade = int(input("enter your grade: "))
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:   
    print("C")
elif grade >= 60:
    print("D")
else:    print("F")
if grade >= 90:
    print("GPA = 4.0")
elif grade >= 80:
    print("GPA = 3.0")
elif grade >= 70:   
    print("GPA = 2.0")
elif grade >= 60:
    print("GPA = 1.0")
else:    print("GPA = 0.0")

#exercise 3

x = int(input("clesius(1) farenheit(2)"))
if x == 1: 
    c = int(input("enter celsius: "))
    f = (c * 9/5) + 32
    print("farenheit: ", round(f, 2))
elif x == 2:
    f = int(input("enter farenheit: "))
    c = (f - 32) * 5/9
    print("celsius: ", round(c, 2))

#exercise 4

loan = int(input("enter loan amount: "))
years = int(input("enter number of years: "))
rate = float(input("enter interest rate: "))
total = loan * (1 + (rate/100) * years)
print("total amount to be paid: ", round(total, 2))
intrest = total - loan
print("total intrest: ", round(intrest, 2))
monthly = total / (years * 12)
print("monthly payment: ", round(monthly, 2))

#exercise 5

numbers= int(input("enter 5 numbers: "))
parts = numbers.split()
nmb=[float(x) for x in parts]
total = sum(nmb)
print("total: ", total)
average = total / len(nmb)
print("average: ", round(average, 2))
highest = max(nmb)
print("highest: ", highest)
lowest = min(nmb)
print("lowest: ", lowest)
