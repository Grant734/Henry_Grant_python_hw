a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

even_numbers = []

for number in a:
    # no remainder
    if number % 2 == 0:
        even_numbers.append(number)

print("Even numbers:", even_numbers)