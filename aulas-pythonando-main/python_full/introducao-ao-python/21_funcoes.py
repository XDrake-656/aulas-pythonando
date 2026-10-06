# Args e Kwargs
# Funções recursivas
# High order function
# Decorators

def calcular_media(num1:float, num2:float, num3=0):
    return (num1 + num2 + num3) / 3
media = calcular_media(4,7,6)
print(f"{media:.2f}")
