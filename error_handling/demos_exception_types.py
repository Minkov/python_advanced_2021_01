# def avg(numbers):
#     return sum(numbers) / len(numbers)
#
#
# ll = [1, 2, 3]
# print(avg(ll))
# #
# ll = []
#
# print(avg(ll))

# print(dd)

# print('2' + 2)
# print(2 + '2')

# print('hello 2')


## Index error
#
# ll = [1, 2, 3]
# # print(ll[0])
# # print(ll[1])
# # print(ll[2])
# # print(ll[3])
#
# n = len(ll)
# # -n <= i < n, i E [-n, n)
# # 0 -> -n
# # 1 -> -n + 1
# # 2 -> -n + 2
# # -3 = n-3
# for i in range(-n, n):
#     print(ll[i])


## KeyError
#
# def get_value_or_none(the_dict, key):
#     if key in the_dict:
#         return the_dict[key]
#     return None
#     # try:
#     #     return the_dict[key]
#     # except KeyError:
#     #     return None
#
#
# dd = {
#     'a': 1,
#     'b': 2,
#     'c': 3,
# }
#
# print(get_value_or_none(dd, 'a'))
# print(get_value_or_none(dd, 'z'))


## TypeError
#
# # print(2 + '2')
# print(', '.join([1, 2, 3, 4]))

## ValueError

print(int('123'))
print(int('abc', base=16)) # 10 * 16^2 + 11*16^1 + 12 * 16^0