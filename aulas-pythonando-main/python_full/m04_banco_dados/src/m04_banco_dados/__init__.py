from funcao import saudacao
from treino import verificar_idade


def main():
    print(saudacao("Estudante"))
    status = verificar_idade(25)
    print(f"Status no sistema: {status}")
