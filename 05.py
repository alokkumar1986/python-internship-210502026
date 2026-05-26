 # Python program using method to check odd or even

def check(num):
    if num % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

n = int(input("Enter a number: "))
check(n)