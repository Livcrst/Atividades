def contador():
  gols = int(input("Saldo de gols: "))
  empates = int(input("Saldo de empates: "))
  vitorias = int(input("Saldo de vitorias: "))

  return gols,empates, vitorias

def calculo ():
  cont = contador()
  valor = (cont[2]*3)+(cont[1]*1)
  return valor,cont

print("######Tabela do Campeonato#########")

print("Dados do time 1")
conta = calculo()


print("Dados do time 2")
cont = calculo()


for i in range(10):
  print("Carregando resultados ...")

if conta[0] > cont[0]:
  print("Resultado: Time 1")
elif conta[0] < cont[0]:
  print("Resultado: Time 2")
else:
  if conta[1][0] > cont[1][0]: 
    print("Resultado: Time 1") 
  elif conta[1][0] < cont[1][0]:
    print("Resultado: Time 2")
  else:
    print("RESULTADO: Empate")