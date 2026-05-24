#Write a program to enter a two digit number and print it in words.

num = int(input("Enter a two-digit number: "))

ones = ["", "One", "Two", "Three", "Four", "Five",
        "Six", "Seven", "Eight", "Nine"]

tens = ["", "", "Twenty", "Thirty", "Forty",
        "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

if 10 <= num <= 19:
    special = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen",
               "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    print(special[num - 10])
elif 20 <= num <= 99:
    print(tens[num // 10], ones[num % 10])
else:
    print("Invalid input")