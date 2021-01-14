# tt = (1, 2, 3)
# print(tt)
#
# print(tt[0])
# print(tt[-1])
#
# for x in tt:
#     print(x)
#
# print(sum([1, 2, 3]))
# print(sum((1, 2, 4)))
# print(sum(map(lambda x: x + 1, tt)))
#
# tt1 = (1,)
# print(tt1)
#
# tt_empty = ()
# print(tt_empty)
#
#
# def find_min_max(numbers):
#     min_number = min(numbers)
#     max_number = max(numbers)
#
#     return (min_number, max_number)
#
#
# (min_number, max_number) = \
#     find_min_max((1, 2, 3, 4, 5, 6, 7, 8))
# print(min_number)
# print(max_number)
#
# names_marks = {
#     'Pesho': 5.5,
#     'Gosho': 3,
# }
#
# for (name, mark) in names_marks.items():
#     print(f'{name} -> {mark}')


# |N|N|N|N|, count = 0, capacity = 4
# append(X)
# |X|N|N|N|, count = 1, capacity = 4
# append(X)
# append(X)
# append(X)
# |X|X|X|X|, count = 4, capacity = 4
# append(Y)
# |X|X|X|X|Y|N|N|N|, count = 5, capacity = 8


# tt = (1, 2, 3)
# tt2 = (5,)
# print(tt)
# print(tt2)
# tt_result = tt + tt2
# print(tt_result)
#
# def get_indices(values, value):
#     index = 0
#     indices = []
#     while True:
#         try:
#             new_index = values.index(value, index)
#             indices.append(new_index)
#             index = new_index + 1
#         except ValueError:
#             break
#
#     return indices
#
#
# tt = (1, 2, 2, 3, 1)
# print(get_indices(tt, 1))
# print(get_indices(tt, 2))

# tuple_of_lists = ([1], [2, 3], [3, 4, 5])
#
# print(tuple_of_lists)
# tuple_of_lists[1].append(-1)
# print(tuple_of_lists)
#
# tt = (1, 2, 3)
# x = tt[0]
# y = tt[1]
# z = tt[2]
# print(x, y, z)
#
# a, b, c = tt
# print(a, b, c)
# print(a)
# print(b)
# print(c)
#
# i, *rest = tt
# print(i, rest)
#
# # tt = ('1 2 3',)
# # tt[0] = tt[0].split()
# # print(type(tt))
# # print(tt)

# tt2 = ('1', '2', '3')
# print(tt2)
print(sorted(['8', 'a', 'A', '_']))