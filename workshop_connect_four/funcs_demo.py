def get_func(sign):
    def sum(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    if sign == '+':
        return sum
    else:
        return subtract


f = get_func('+')
s = get_func('-')
print(f(2, 3))
print(s(2, 3))
