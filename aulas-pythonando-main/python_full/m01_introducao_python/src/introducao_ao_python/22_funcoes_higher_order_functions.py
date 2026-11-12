def validar(x):
     return x

def soma(x, y):
     return x + y

print(validar) #{Retona: a referencia de memoria}

print(validar(soma)(2, 3)) #{Retona: 5}
