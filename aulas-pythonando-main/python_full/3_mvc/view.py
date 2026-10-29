from controller import PersonController

while True:
    question = int(input("Digite 1 para SALVAR uma pessoa, digite 2 para VER a pessoa e 3 para SAIR: "))
    if question == 3:
        break
    if question == 1:
        name = input("Digite seu nome: ").title().strip()
        age = int(input("Digite sua idade: "))
        cpf = input("Digite seu cpf: ").strip()
        
        if PersonController.sing_up(name, age, cpf):
           print("Usuario cadastrado com sucesso")
        else:
            print("digite valores validos")
