# text = 'ILOvePython'

VOWELS = {'a', 'o', 'u', 'e', 'i'}
VOWELS = VOWELS.union(x.upper() for x in VOWELS)
# [VOWELS.add(x.upper()) for x in list(VOWELS)]

# result = []
# for ch in text:
#     if ch not in VOWELS:
#         result.append(ch)
#
# print(result)

text = input()
result = [ch for ch in text if ch not in VOWELS]
print(''.join(result))
