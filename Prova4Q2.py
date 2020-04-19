#Questão2
def dados():
    nome = input("Digite nome do candidato: ")
    idade = int(input("Digite idade do candidato: "))
    votos = int(input("Digite votos do candidato: "))

    dados = (nome,idade,votos)

    return dados

lista = []
n = int(input("Digite qntd de candidatos: "))
while True:
    
    if len(lista) == n :
        break
    else:
        dd = dados()
        lista.append(dd)
def maxi(lista):
    maior = (0,0,0)
    for i in range(len(lista)):
        if lista[i][2] > maior[2]:
            maior = lista[i]
        else:
            pass
    return maior

maxiList = []
itemMax = maxi(lista)
for i in lista:
    if i[2] == itemMax[2]:
        maxiList.append(i)
    else:
        pass

if len(maxiList) > 1:
    maxidade = (0,0,0)
    listIdad = []
    for i in range(len(maxiList)):
        if maxiList[i][1] > maxidade[1]:
            maxidade = maxiList[i]
        else:
            pass
    for k in maxiList:
        if k[1] == maxidade[1]:
            listIdad.append(k)
        else:
            pass
    if len(listIdad) > 1:
        ordenado = sorted(listIdad)
        print("{} venceu".format(ordenado[0][0]))
    else:
        print("{} venceu".format(listIdad[0][0]))