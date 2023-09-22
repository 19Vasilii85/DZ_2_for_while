s = int(input('Введите сумму числа: '))
p = int(input('Введите произведение числа: '))
for x in range(s):
    for y in range(s):
        if x + y == s and x * y == p:
            print(x, y)