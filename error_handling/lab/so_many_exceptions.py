# numbers_list = input().split(", ")
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
result = 1

for number in numbers_list:
    if number <= 5:
        result *= number
    elif number <= 10:
        result /= number

print(result)
