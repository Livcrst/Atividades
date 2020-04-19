def conj ():
    lista = []
    while True:
        n = int(input("Para sair digite 0.\n Digite numero a ser adicionado: "))
        if n == 0:
            break
        else:
            lista.append(n)
    return lista
lista1 = conj()
lista2 = conj()

def inter(lista,listaum):
    v = set(lista)
    value = set(listaum)
    if v.intersection(value) == False:
        return "Não"
    else:
        return "Sim"

print(inter(lista1,lista2))