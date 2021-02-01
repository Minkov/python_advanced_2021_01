from lab.math_operations.math_operations import calculate_expression


expressions = [
    '2.5 * 2',
    '6.66 ^ 2',
    '36.66 / 6',
    '44.44 + 6',
    '44.44 - 4',
]

[print(calculate_expression(x)) for x in expressions]
