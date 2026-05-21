#Write a program to enter a two digit number and print it in words.
def number_to_words(n: int) -> str:
    if n < 10 or n > 99:
        return "Input must be a two-digit number."

    units = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    if 10 <= n < 20:
        return teens[n - 10]
    else:
        ten_part = tens[n // 10]
        unit_part = units[n % 10]
        return f"{ten_part} {unit_part}".strip()
    
print(number_to_words(12))