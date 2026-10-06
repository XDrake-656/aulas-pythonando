"""
def fatorial(n: int) -> int:
    #caso base: quando ele chegar ao valor de 1 ele continua o codigo
    if n == 1:
        return 1 
    #caso recursivo: faz um loop salvando na memoria todos os valores da fatorial ate que ele retorne o return e volte o codigo ate calcular todos os valores salvos
    return n * fatorial(n - 1)

fat = fatorial(5)
print(fat)
"""
from collections import namedtuple

Box = namedtuple("Box", "have_key")

def find_key(boxes: list[Box], index: int = 0) -> Box:
    #caso base: se o índice passar do tamanho da lista, a chave não foi encontrada
    if len(boxes) <= index:
        return Box(False)
    
    curent_box = boxes[index]
    print(f"Buscando chave na caixa de indece {index} => {Box}")
    
    #caso base: se a caixa atual tem a chave, retorna ela
    if curent_box.have_key:
        return curent_box
    
    # caso recursivo: avança para o próximo índice
    index += 1
    return find_key(boxes, index)    
    
boxes : list[Box] = [
    Box(False), Box(False), Box(True),
    Box(False), Box(False), Box(False),
    Box(False), Box(False), Box(False),
    ]

print(find_key(boxes))
