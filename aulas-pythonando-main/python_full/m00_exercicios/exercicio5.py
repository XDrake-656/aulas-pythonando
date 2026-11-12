numbres = (input())
numbers_list = []
for n in range(len(numbres)):
    if numbres[n].isnumeric():
        numbers_list.append(int(numbres[n]))

if len(numbers_list) != len(set(numbers_list)):
    print("Existem elementos duplicados!")
else:
    print("Nenhum elemento duplicado!")
