produtos = [{'nome': 'Celular', 'preco': 2000.0, 'categoria': 'Eletronico'}, {'nome': 'Coca cola', 'preco': 6.0, 'categoria': 'bebidas'}]

while True:
    decisao = input('Digite N para um novo produto ou S para sair: ').upper()

    if decisao == 'S':
        break

    nome = input('Nome: ')
    preco = float(input('Preço: '))
    categoria = input('Categoria: ')
    produto = {
        'nome': nome,
        'preco': preco,
        'categoria': categoria
    }

    produtos.append(produto.copy())

print(produtos)
soma = 0
for i in produtos:
    soma += i['preco']

print(soma)
