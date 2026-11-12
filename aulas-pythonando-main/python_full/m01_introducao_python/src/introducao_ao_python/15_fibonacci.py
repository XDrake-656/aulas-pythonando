seq = int(input("Digite quantos numeros voce quer da sequencia de fibonacci: "))
f0 = 0
f1 = 1
f2 = 0
for f in range(seq):
    print(f2, end=" ")
    f0 = f1
    f1 = f2
    f2 = f0 + f1
print("fim")
