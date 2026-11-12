x = []
while True:
    nota = float(input("digite a nota[-1 para parar]: "))
    if nota == -1:
        break
    x.append(nota)
soma = cont = 0
for c in x:
    soma += c
    cont += 1
print(soma/cont)
