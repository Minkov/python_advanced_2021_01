def max_number(numbers):
    best = numbers[0]

    for number in numbers:
        if best < number:
            best = number

    return best


def max_number_rec(numbers):
    if len(numbers) == 1:
        return numbers[0]

    x = numbers[-1]
    y = max_number_rec(numbers[:-1])

    return x if y < x else y


print(max_number([1, 7, 2, 3, 4, 5]))
print(max_number_rec([1, 7, 2, 3, 4, 5]))

# 1 2 3
# 1+2+3
# 1+2-3
# 1-2+3
# 1-2-3
# -1+2+3
