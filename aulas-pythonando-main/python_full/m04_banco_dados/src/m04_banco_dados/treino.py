def verificar_idade(idade):
    if idade >= 18:
        return "Maior de idade"
    return "Menor de idade"


# Tudo que estiver abaixo só roda se você executar ESTE arquivo diretamente
if __name__ == "__main__":
    print("--- Rodando teste local do arquivo treino.py ---")
    print("Teste com 20 anos:", verificar_idade(20))
    print("Teste com 15 anos:", verificar_idade(15))
