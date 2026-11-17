# 🐍 Módulo 01: Preparando o Ambiente e Fundamentos

## Preparando o Ambiente (`uv`, `ruff` e `mypy`)
* **Criar projeto:** `uv init NomeDaPasta`
* **Criar ambiente virtual:** `uv venv`
* **Sincronizar venv com `pyproject.toml`:** `uv sync`
* **Instalar bibliotecas (produção):** `uv add biblioteca`
* **Instalar bibliotecas (desenvolvedor):** `uv add --dev biblioteca`

### Qualidade e Tipagem
* **Adicionar Ruff:** `uv add ruff`
* **Checar código:** `uv run ruff check`
* **Corrigir erros automaticamente:** `uv run ruff check --fix`
* **Formatar e limpar o código:** `uv run ruff format`
* **Adicionar Mypy:** `uv add mypy`
* **Checar tipagem:** `uv run mypy arquivo.py`

Para ignorar alguma regra específica no `pyproject.toml`:
```toml
[tool.ruff.lint]
ignore = ["CODIGO_DO_ERRO"]
```

---

## Variáveis e Tipos Primitivos
* **Definição:** Espaços nomeados dentro da memória RAM. São **mutáveis**.
* **Boas práticas:** Não comece com números ou caracteres especiais, não use palavras reservadas do Python e use letras minúsculas separadas por underline (ex: `vida_jogador`).

### Tipos Primitivos
* `int`: Valores inteiros (`7`, `-4`, `0`, `9875`).
* `float`: Valores flutuantes/decimais (`4.5`, `0.076`, `-15.223`, `7.0`).
* `bool`: Valores lógicos (`True`, `False` — sempre com a primeira letra em maiúsculo).
* `str`: Strings/textos (`'ola'`, `'7.5'` — strings ficam sempre entre **aspas** simples ou duplas).

---

## Operadores

### Operadores Aritméticos (Ordem de Precedência)
1. `()` — Parênteses
2. `**` ou `pow()` — Potência
3. `*` (multiplicação), `/` (divisão), `//` (divisão inteira), `%` (resto da divisão)
4. `+` (soma), `-` (subtração)

### Operadores Relacionais
* `>` (maior), `<` (menor), `==` (igual), `>=` (maior ou igual), `<=` (menor ou igual), `!=` (diferente).

### Operadores Lógicos
* `and`: Retorna `True` apenas se **ambas** as condições forem verdadeiras.
* `or`: Retorna `True` se **pelo menos uma** condição for verdadeira.
* `not`: Inverte o resultado (`False` vira `True`, e `True` vira `False`).

---

## Módulos e Pacotes
Um módulo é um arquivo `.py` com código reutilizável. Ele ajuda na **organização**, **reutilização** (evita repetição) e **escopo** (cada módulo tem seu próprio *namespace*).

* `import modulo`: Importa o módulo inteiro.
* `from modulo import item`: Importa algo específico.
* `pip install pacote`: Instala bibliotecas externas pelo terminal (ou `uv add pacote`).

---

## Manipulação de Strings (Texto)

### Fatiamento
```python
texto = "Curso de Python"
print(texto[0:5:1])  # [início : fim : passo]
```

### Análise e Transformação
* `len(variavel)`: Mostra o tamanho (quantidade de caracteres/itens).
* `variavel.count('x', inicio, fim)`: Conta quantas vezes `'x'` aparece.
* `variavel.find('x')`: Mostra o índice onde `'x'` começa (retorna `-1` se não achar).
* `variavel.index('x')`: Igual ao `find()`, mas gera erro se não encontrar.
* `'x' in variavel`: Retorna `True` ou `False` se `'x'` estiver na variável.
* `variavel.replace('velho', 'novo')`: Substitui trechos de texto.
* `variavel.upper()` / `variavel.lower()`: Tudo em maiúsculas / minúsculas.
* `variavel.capitalize()`: Apenas a primeira letra da frase em maiúscula. *(⚠️ [CORREÇÃO: Estava escrito "captaliza()"])*
* `variavel.title()`: Primeira letra de cada palavra em maiúscula.
* `variavel.strip()`: Remove espaços inúteis no início e no fim. *(⚠️ [CORREÇÃO: Estava com vírgula "variavel,strip()"])*
* `variavel.rstrip()` / `variavel.lstrip()`: Remove espaços apenas da direita / esquerda.

### Divisão e Junção
* `variavel.split()`: Divide uma string em uma lista de palavras.
* `'-'.join(lista)`: Junta itens de uma lista em uma única string usando `'-'`.

---

## Cores no Terminal (ANSI Escape Sequences)
Sintaxe: `\033[X;Y;Zm`: X = Style, Y = Text, Z = Back 

| Style (Estilo)  | Text (Cor do Texto) | Back (Cor de Fundo) |
| :-------------- | :------------------ | :------------------ |
| `0` = None      | `30` = Branco/Preto | `40`                |
| `1` = Bold      | `31` = Vermelho     | `41`                |
| `4` = Underline | `32` = Verde        | `42`                |
| `7` = Negative  | `33` = Amarelo      | `43`                |
|                 | `34` = Azul         | `44`                |
|                 | `35` = Roxo         | `45`                |
|                 | `36` = Ciano        | `46`                |
|                 | `37` = Cinza        | `47`                |

---

## Estruturas de Controle e Repetição

### Condicionais (`if`, `elif`, `else`)
```python
if condicao:
    # bloco 1
elif outra_condicao:
    # bloco 2
else:
    # bloco 3

# Condição simplificada (Operador Ternário):
print("Sim" if x == 10 else "Não")
```

### Laços de Repetição (`for`, `while`, `break`, `continue`)
```python
# FOR: repete um número definido de vezes
for i in range(1, 10):
    print(i)

# WHILE: repete enquanto a condição for verdadeira
while not acertou:
    if sair:
        break     # Interrompe o laço imediatamente
    if pular:
        continue  # Volta para o início do laço sem executar o resto
```
