cpf = input('Digite o seu CPF? ')
firstDigits = "";
cpf_formated = ""
for e, i in enumerate(cpf):
        if i != '.' and i != '-':
           cpf_formated += i
        if e <= 10 and i != '.' and i != '-':
            firstDigits += i
total = 0
for e, value in enumerate(range(10, 1, -1)):
    value = int(value)
    v = firstDigits[e]
    v = int(v)
    v *= value
    total += v

resultD1 = 11 - (total % 11)
resultD1 = 0 if resultD1 > 9 else resultD1
print(f"Digito 1 = {resultD1}")
firstDigits += str(resultD1)
totalD2 = 0
for e, value in enumerate(range(11, 1, -1)):
    value = int(value)
    v = firstDigits[e]
    v = int(v)
    v *= value
    totalD2 += v
resultD2 = 11 - (totalD2 % 11)
firstDigits += str(resultD2)
novo_cpf = firstDigits
print(f'Digito 2 = {resultD2}')
if novo_cpf == cpf_formated:
    print("Válido")
else:
    print("Inválido")