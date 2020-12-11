
from random import randint
number = str(randint(100000000, 999999999))

new_cpf = number
reverse = 10
total = 0
d = 0
for index in range(19):
    if index > 8:
        index -= 9

    total += int(new_cpf[index]) * reverse

    reverse -= 1
    if reverse < 2:
        reverse = 11
        d = (11 - (total % 11))
        if d > 9:
            d = 0
        else:
            d == d
        total = 0
        new_cpf += str(d)
print(new_cpf)