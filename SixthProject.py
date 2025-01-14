def find_numbers(numbers, target):
    for i in range (len(numbers)):
        for x in range(i + 1, len(numbers)):
            if numbers[i] + numbers[x] == target:
                return [i, x]

numbers = [2, 7, 8, 11, 15]
target = 9

result = find_numbers(numbers, target)

print("Indices of numbers that add up to target:", result)