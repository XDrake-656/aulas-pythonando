def validar(f):
     def valida(x, y):
          if x < 0 or y < 0:
               raise ValueError("x e y nao podem ser negativos")
          return f(x, y)
     return valida

@validar
def soma(x, y):
     return x + y

print(soma(10, -20))
