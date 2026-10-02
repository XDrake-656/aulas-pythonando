# +,-,*,/,//,%,**

valor_comida = float(input("Digite o valor da comida: "))
valor_bebida = float(input("Digite o valor da bebida: "))
valor_cupom = int(input("Digite o valor do cupom: "))
entrega = float(input("Digite o valor da entrega: "))
taxa_percentual = int(input("Taxa: "))

valor = (valor_comida + valor_bebida + entrega) - valor_cupom
taxa = valor * (taxa_percentual/100)

final = valor + taxa

print(valor)
print(taxa)
print(final)
