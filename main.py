from funciones import(
    borrdup,
    ordenar,
    eliminarimpar,
    sumaryañadir
)

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