# 📦 Módulo 02: Variáveis Compostas (Estruturas de Dados)

## 1. Tuplas `()` — Imutáveis
Sequência ordenada de elementos que **não pode ser alterada** depois de criada.
usamos `()` para escrever uma tupla porem **para referenciala** no codigo usamos `[]` 

```python
lanche = ("Hambúrguer", "Suco", "Pizza", "Pudim")
print(lanche[0])    # Hambúrguer
print(lanche[1:3])  # ('Suco', 'Pizza')

# Apagando a tupla inteira (não é possível apagar apenas um item)
del lanche
del lanche[0] #(gerará `TypeError` porque tuplas são imutáveis)
```

---

## 2. Listas `[]` — Mutáveis
Sequência ordenada que **pode ser modificada** a qualquer momento.

### Adicionando e Ordenando
```python
lista = list()            # Cria uma lista vazia
lista = ["A", "B", "C"]   # Cria uma lista com itens desejados
lista[0] = "Z"            # Substitui o item na posição 0
lista.append("D")         # Adiciona no final
lista.insert(1, "X")      # Adiciona na posição 1
lista.sort()              # Ordena em ordem crescente/alfabética
lista.sort(reverse=True)  # Ordena ao contrário
sum(numeros)              # Soma valores numéricos da lista
```

### Copiando Listas (Cuidado com referência!)
```python
# ❌ ERRADO (Cria uma ligação/referência entre as duas):
a = [1, 2]
b = a
b[0] = 99  # Altera 'a' também!

# ✅ CERTO (Cria uma cópia independente):
b = a[:]
# ou
b = a.copy()
```

### Removendo Elementos
```python
del lista[0]           # Apaga pelo índice
lista.pop()            # Apaga o último item (ou o índice passado em pop(x))
lista.clear()          # Esvazia a lista sem apagar a variável

# Evitando erro caso o item não exista:
if "B" in lista:
    lista.remove("B")  # Remove a primeira ocorrência do valor
```

### Listas Compostas (Listas dentro de Listas)
```python
galera = [["João", 19], ["Ana", 33], ["Joaquim", 50]]
print(galera[0][1])  # 19
print(galera[2][0])  # Joaquim
```

### List Comprehension
Sintaxe curta para criar listas a partir de iteráveis:
lista = [expression for c in iterable if condition == True]
```python
# ⚠️ [Evite nomear variáveis como "list", pois sobrescreve a função nativa do Python]
numeros_maiores = [i for i in range(10) if i > 4]
print(numeros_maiores)  # [5, 6, 7, 8, 9]
```

---

## 3. Dicionários `{}` — Chave e Valor
Armazenam dados usando chaves personalizadas em vez de índices numéricos. São **mutáveis**.

```python
# Valor Chave e Itens:
filme.values()  # variaveis dentro dos elementos
filme.keys()    # elementos dos dicionarios
filme.items()   # mostra tanto os elementos quanto suas variaveis

filme = {"titulo": "Star Wars", "ano": 1977, "diretor": "George Lucas"}

# Adicionar ou atualizar
filme["nota"] = 9.5

# Buscar com segurança (retorna valor padrão se a chave não existir)
print(filme.get("bilheteria", "Não informado"))

# Remover chave
del filme["nota"]

# Percorrendo chaves e valores
for chave, valor in filme.items():
    print(f"O {chave} é {valor}")

# Copiando dicionário (fatiamento [:] não funciona em dicionários)
copia_filme = filme.copy()

#pode se ter dicionarios dentro de listas:
locadora = [{"titulo":"Star Wars", "Ano":"1977", "diretor":"George Lucas"}, {"titulo":"Matrix", "Ano":"1999", "diretor":"Wachowski"}]
print(locadora[0]["Ano"])       #: 1977
print(locadora[1]["titulo"])    #: Matrix
```
---

## 4. Conjuntos (`set`) — Valores Únicos
Coleção não ordenada que **não aceita valores duplicados**.

```python
# ⚠️ Nunca use {} vazio para criar um set, pois {} cria um dicionário!
conjunto_a = set([1, 2, 3])  # conjunto
conjunto_b = {3, 4, 5}       # dicionario

conjunto_a.union(conjunto_b)                 # União: {1, 2, 3, 4, 5}
conjunto_a.intersection(conjunto_b)          # Interseção: {3}
conjunto_a.difference(conjunto_b)            # Diferença: {1, 2}
conjunto_a.symmetric_difference(conjunto_b)  # Diferença simétrica: {1, 2, 4, 5}
```
