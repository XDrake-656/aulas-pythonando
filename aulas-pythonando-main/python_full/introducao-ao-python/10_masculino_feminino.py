sexo = input("Qual seu sexo [M/F]: ").strip().upper()[0]
if sexo == "F":
    print("Feminino")
elif sexo == "M":
    print("Masculino")
else:
    print("Você digitou uma opção não valida!!!")
