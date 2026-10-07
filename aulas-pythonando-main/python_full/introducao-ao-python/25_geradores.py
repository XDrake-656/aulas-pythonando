from pympler.asizeof import asizeof


def dobro(lista):
    lista_dobro = []
    for i in lista:
        lista_dobro.append(i * 2)
    return lista_dobro

def dobro_2(lista):
    for i in lista:
        yield i * 2
    


x = dobro(range(10))
print(x)
print(asizeof(x))
print("="*30)
y = dobro_2(range(10))
print(next(y,"fim"))
print(next(y,"fim"))
print(next(y,"fim"))
print(asizeof(y))
print("="*30)
lista = list(dobro_2(range(10)))
print(lista)
print(asizeof(lista))
print("="*30)



