# ⚙️ Módulo 03: Funções, Tratamento de Erros e Geradores

## Funções (`def`) e Boas Práticas
* **PEP 8:** Nomes de funções em letras minúsculas separados por underline (`minha_funcao()`).
* **Docstrings:** Documentação escrita entre três aspas duplas `"""..."""` logo abaixo do `def`. Pode ser lida com `help(minha_funcao)` ou `minha_funcao.__doc__`.
* **Call Stack (Pilha de Chamada):** Memória onde o Python guarda o estado das variáveis locais enquanto uma função está rodando, sabendo para onde voltar após o `return`.

### Parâmetros Opcionais e Tipagem
```python
def configurar(x: int = 0, y: float = 0.0, texto: str = "exemplo", ativo: bool = True):
    """o programa pode funcionar mesmo sem Parametros ja que ele possui Parametros ja declarados"""
    return texto
```

### `*args` e `**kwargs`
* `*args`: Recebe vários argumentos posicionais e empacota em uma **tupla**.
* `**kwargs`: Recebe vários argumentos nomeados e empacota em um **dicionário**.

```python
def somar(*numeros):
    return sum(numeros)

def exibir_dados(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")
```

### Escopo de Variáveis (`global` vs `local`)
Variáveis criadas dentro de funções são **locais** e não afetam variáveis fora dela, a menos que você use a palavra-chave `global` (o que deve ser evitado na maioria dos casos).

```python
def teste_a(b):
    b+= 4
    c = 2

a = 5
teste_a(a)    # escopo global: a = 5 — reconhece apenas o valor de `a` ja que ele era o unico valor no escopo global
              # escopo local:a = 5, b = 9 e c = 2 — reconhece todos os valares

def teste_b(b):
    global a
    a = 8
    b+= 4
    c = 2  

a = 5
teste(a)    # escopo global: a = 8
            # escopo local:a = 8, b = 9 e c = 2 — variavel mudou de valor ja que mesmo localmente voce fez o python considerar ela globalmente
```

**ATENÇÃO** caso um variavel seja declarada no escopo local ela passa ser uma outra variavel se nao ultilizar a palavra-chave `global`
```python
def teste_c(b):
    a = 8
    b+= 4
    c = 2  

a = 5
teste_c(a)      # escopo local:a = 8, b = 9 e c = 2
                # escopo global: a = 5

```

---

## Recursividade
Quando uma função chama a si mesma. Precisa obrigatoriamente de um **Caso Base** (parada) e um **Passo Recursivo**.
* **Vantagens:** Deixa o código mais limpo e elegante para resolver problemas complexos como estruturas de árvores ou "algoritmos de busca".
* **Cuidados:** O uso incorreto ou a falta do caso base gera um erro de stack overflow (estouro de pilha) por esgotar a memória do computador.
* **Consumo de Memória alto:** A cada chamada consome espaço na memória (Call Stack) até atingir o caso base ou o limite.

```python
def fatorial(n: int) -> int:
    if n == 1:  # Caso base
        return 1
    return n * fatorial(n - 1)  # Passo recursivo
```
> **Atenção:** Cada chamada ocupa espaço na *Call Stack* (limite padrão de ~1000 chamadas). Para laços simples, prefira `for` ou `while`.
> **Curiosidade** Pode se almentar o limite padrão de~1000 chamadas com um comando:
```python
from sys import setrecursionlimit
setrecursionlimit(X) # ⚠️CUIDADO OA USAR: ESSE LIMITE EXISTE POR UM MOTIVO
```

---

## Higher-Order Functions, Decoradores e Lambda

### Decoradores (`@`)
Modificam ou estendem o comportamento de uma função sem alterar o código interno dela:
```python
def validar_positivo(func):
    def wrapper(x, y):
        if x < 0 or y < 0:
            raise ValueError("x e y não podem ser negativos")
        return func(x, y)
    return wrapper

@validar_positivo
def soma(x, y):
    return x + y
```

### Funções Anônimas (`lambda`) com `map`, `filter` e `sorted`
```python
numeros = [1, 2, 3, 4, 5]

duplicados = list(map(lambda x: x * 2, numeros))          # [2, 4, 6, 8, 10]
impares = list(filter(lambda x: x % 2 != 0, numeros))     # [1, 3, 5]

alunos = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
ordenados = sorted(alunos, key=lambda x: x[1])            # Ordena pela idade e nao pelo nome
```

---

## Tratamento de Erros e Exceções
* **Erro de Sintaxe:** Código escrito errado (ex: `primt(x)`).
* **Exceção:** Código escrito certo, mas falha na execução (ex: `ValueError` ao digitar texto num `int(input())`).

```python
try:
    numero = int(input("Digite um número: "))
except ValueError:
    print("Você não digitou um número inteiro válido.")
except Exception as erro:
    print(f"Erro inesperado: {erro}")
else:
    print(f"Sucesso! Número: {numero}")
finally:
    print("Bloco executado sempre, com ou sem erro.")
```

* `raise`: Força um erro manualmente (`raise ValueError("Valor inválido")`).
* `assert`: Testa uma condição; se for falsa, gera um `AssertionError`:
```python
x = "hello"
if not isinstance(x, int):
    raise TypeError("Apenas inteiros são permitidos")
```

---

## Iteráveis, Iteradores e Geradores (`yield`)

### Diferença Fundamental
* **Iterável:** Contêiner reutilizável (listas, strings). Implementa `__iter__()`.
* **Iteráveis são reutilizáveis:** Você pode rodar um laço for na mesma lista dezenas de vezes. Ela sempre reinicia do primeiro elemento.
* **Iterador:** Objeto que percorre os dados um por um e se esgota no final. Implementa `__iter__()` e `__next__()`.
* **Iteradores são descartáveis ("esgotáveis"):** Uma vez que você percorreu um iterador até o final usando next(), ele fica vazio. Se tentar usá-lo de novo, ele continuará lançando StopIteration. Para ler os dados novamente, 
você precisa criar um novo iterador ou adicionar um valor de retorno padrão.


Como eles trabalham juntos (O segredo do laço for):
```python
lista = [10, 20, 30]
for item in lista:
    print(item)
```

o Python faz exatamente o seguinte:
1. Pede o iterador: Ele passa o iterável (lista) para a função iter(). Ela ativa o método lista.__iter__(), que devolve um objeto iterador.
2. Consome os itens: O Python chama repetidamente a função next(iterador). Ela ativa o método __next__() para entregar um elemento por vez.
3. Para no final: Quando os dados acabam, o iterador lança uma exceção chamada StopIteration. O laço for entende isso como um sinal de parada e termina o código de forma limpa.



### Geradores e Memória RAM
O Python gerencia memória usando um **Heap Privado** e **Contagem de Referências**. Geradores usam `yield` em vez de `return` para entregar **um item por vez**, evitando estourar a RAM ao ler arquivos de vários GB.

```python
def ler_linhas(nome_arquivo: str):
    with open(nome_arquivo) as f:
        for linha in f:
            yield linha  # Entrega uma linha por vez sob demanda

def filtrar_erros(linhas):
    for linha in linhas:
        if "CRITICAL" in linha:
            yield linha

# Pipeline conectado (consome quase zero de RAM)
for erro in filtrar_erros(ler_linhas("sistema.log")):
    print(f"[LOG CRÍTICO] -> {erro.strip()}")
```

---

## Manipulação de Arquivos (`open` e `with`)
* Modos: `"r"` (leitura), `"w"` (escrita/sobrescreve), `"a"` (anexa no final), `"x"` (cria novo), `"b"` (binário).
* Use sempre `with open(...)` para garantir que o arquivo seja fechado automaticamente.
* **`pickle`:** Módulo para serializar objetos Python em bytes (`dump`, `dumps`, `load`, `loads`). Nunca carregue arquivos `pickle` de fontes não confiáveis.
