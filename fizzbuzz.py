# Fizzbuzz
# from number 1-100
# If a number is divisible by 3, print fizz
# If a number is divisible by 5, print buzz
# If a number is divisible by both, print fizzbuzz

# This is an example off fizzbuzz code
"""
for num in range (1,100):
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    else:
        print(num)
"""
import time
# Now let's make this fizzbuzz program into a function
choice = int(input("What number would you like to choose? "))

def fizzbuzz(choice):
    for i in range(1,choice):
        if i % 3 == 0:
            if i % 5 == 0:
                print(str(i) + " fizzbuzz")
            else:
                print(str(i) + " fizz")
        elif i % 5 == 0:
            if i % 3 == 0:
                print(str(i) + " fizzbuzz")
            else:
                print(str(i) + " buzz")
        else:
            print(i)

print("About to run the program")
time.sleep(1)
fizzbuzz(choice)