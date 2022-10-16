def borrdup(lis):
    lis2 = []
    for i in lis:
        if i in lis2:
            continue
        else:
            lis2.append(i)
    return lis2

def ordenar(lis):
    lis.sort(reverse= True)
    return lis

def eliminarimpar(lis):
    for i in lis:
        if i//2 ==0:
            continue
        else:
            lis.remove(i)
    return lis

def sumaryañadir(lis):
    suma = sum(lis)
    lis.insert(0, suma)
    return lis


def modificar(listainicial):
    lista =borrdup(listainicial)
    lista = ordenar(lista)
    lista = eliminarimpar(lista)
    lista = sumaryañadir(lista)
    return lista




lista = [3,5,7,4,6,8,5,3,4,6,8,9,3,4,3,5]
nueva_lista = modificar(lista)
print(nueva_lista)
print( nueva_lista[0] == sum(nueva_lista[1:]) )