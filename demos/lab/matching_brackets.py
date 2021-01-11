expression = input()

s = []

for i in range(len(expression)):
    ch = expression[i]
    if ch == '(':
        s.append(i)
    elif ch == ')':
        j = s.pop()
        print(expression[j:i + 1])
