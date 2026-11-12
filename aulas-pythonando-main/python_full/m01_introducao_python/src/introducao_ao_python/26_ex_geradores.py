# --- PASSO 1: CRIAR O ARQUIVO DE TESTE AUTOMATICAMENTE ---
# Este bloco serve apenas para gerar o arquivo 'sistema.log' na mesma pasta para você testar
def criar_arquivo_exemplo():
    conteudo_log = """2026-10-07 10:00:01 INFO Sistema inicializado com sucesso.
2026-10-07 10:02:15 DEBUG Conexão com o banco de dados estabelecida.
2026-10-07 10:05:42 WARNING Uso de memória acima de 70%.
2026-10-07 10:10:19 CRITICAL Falha na sincronização do sistema de arquivos.
2026-10-07 10:12:03 INFO Usuário 'admin' fez login com sucesso.
2026-10-07 10:15:30 DEBUG Processamento em segundo plano finalizado.
2026-10-07 10:20:00 CRITICAL Conexão perdida com a API de pagamentos secundária.
2026-10-07 10:22:11 INFO Verificação de rotina concluída.
"""
    with open("sistema.log", "w", encoding="utf-8") as f:
        f.write(conteudo_log)
    print("[✓] Arquivo 'sistema.log' criado com sucesso!\n")


# --- PASSO 2: O PIPELINE DE GERADORES ---

def ler_linhas(nome_arquivo):
    """Gerador 1: Abre o arquivo e entrega uma linha por vez"""
    with open(nome_arquivo, "r", encoding="utf-8") as f:
        for linha in f:
            yield linha

def filtrar_erros(linhas):
    """Gerador 2: Recebe as linhas e só repassa as que contêm CRITICAL"""
    for linha in linhas:
        if "CRITICAL" in linha:
            yield linha

def formatar_mensagem(linhas_filtradas):
    """Gerador 3: Modifica o texto final de cada linha filtrada"""
    for linha in linhas_filtradas:
        yield f"[LOG CRÍTICO] -> {linha.strip()}"


# --- PASSO 3: EXECUÇÃO DO CÓDIGO ---
if __name__ == "__main__":
    # Garante que o arquivo de exemplo existe
    criar_arquivo_exemplo()

    # Conectando os geradores (Nenhum processamento de arquivo ocorre aqui ainda)
    fluxo_linhas = ler_linhas("sistema.log")
    fluxo_erros = filtrar_erros(fluxo_linhas)
    fluxo_final = formatar_mensagem(fluxo_erros)

    print("--- Iniciando o consumo do pipeline ---")
    # O laço for consome o pipeline item por item, gastando o mínimo de memória
    for mensagem in fluxo_final:
        print(mensagem)
