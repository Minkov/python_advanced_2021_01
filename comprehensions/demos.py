# ll = [1, 2, 3, 4, 5, 6]
#
# ll1 = [x for x in ll]
# ll1.append(-3)
# print(ll)
# print(ll1)
# print(
#     [x for x in ll]
# )
#
# print(
#     [x + 1 for x in ll]
# )
#
# print(
#     [x + 1 for x in ll if x % 2 == 0]
# )
#
# evens = []
# for x in ll:
#     if x % 2 == 0:
#         evens.append(x + 1)
# print(evens)
#
# lll = [1, 2, 3]
# ddd = {'x': 1}
# sss = {1, 2, 3}

def to_binary(number):
    bits = []
    while number:
        bits.append(number % 2)
        number //= 2
    return ''.join(map(str, bits[::-1]))


ll = [1, 2, 3, 3, 4, 5, 6, 7, 14, 15]

print(
    [True if x % 2 == 0 else False for x in ll]
)

print(
    [x % 2 == 0 for x in ll]
)

print(
    [to_binary(x) for x in ll]
)

print(
    [x * x for x in ll]
)

print(
    {x * x for x in ll}
)

print(
    {x: x * x for x in ll}
)
n = 5
print(
    {x: to_binary(x) for x in ll}
)

print(
    {to_binary(x): x for x in ll}
)

print(
    {to_binary(x): to_binary(x) for x in ll}
)
