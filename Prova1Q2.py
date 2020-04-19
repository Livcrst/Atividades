def media(lista):
    soma = 0
    for i in lista:
        soma += i
    media = soma/len(lista)
    return media

print("##### Inicio de auditoria#####")
print("Digite 0 após inserir todos os salarios a serem verificados.")

salarios = []
while True:
    n = int(input("Digite salário: "))
    if n == 0:
        break
    else:
        salarios.append(n)

acima = []

medi = media(salarios)

for i in range(len(salarios)):
    if salarios[i] > medi:
        acima.append(i)

print(acima)
print("FIM")