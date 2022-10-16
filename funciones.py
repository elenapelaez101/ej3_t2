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
