print("############## Votação da turma #############")

def contador(lista,a):
	cnt = 0
	for i in lista:
		if i == a:
			cnt += 1
		else:
			pass
	return cnt 

#lista =[1, 1, 2, 1, 3, 3, 2, 1, 2, 2, 1, 3]
lista = [2, 2, 2, 1, 1, 2, 3, 2, 1, 2, 3, 2, 1, 3, 3,3,3,3,3,3,3,3,3,3,3,3]

v1 = contador(lista,1)
v2 = contador(lista,2)
v3 = contador(lista,3)

for i in range(len(lista)):
	print("Contado votos ...")


print("RESULTADO: ")

if v1 > v2 and v1 > v3:
	print("Candidato 1")
elif v1 < v2 and v2 > v3:
	print("Candidato 2")
else:
	print("Candidato 3")

