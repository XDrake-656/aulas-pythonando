num = int(input("Digite um numero que voce quer saber se é ou não é primo: "))
cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        cont += 1
        print("\033[1;32m", end="")
    else:
        print("\033[1;31m", end="")
    print(c, "\033[m", end=" ")
        
if cont == 2 or num == 1:
    print("É primo")
else:
    print("Não é primo")
