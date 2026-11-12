sexo = input("Qual seu sexo [M/F]: ").strip().upper()[0]
while sexo not in "MF":
    sexo = input("Valor invalido. Digite apenas [M/F]: ").strip().upper()[0]
if sexo == "F":
    print("Feminino")
elif sexo == "M":
    print("Masculino")
