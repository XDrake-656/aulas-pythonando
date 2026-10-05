n1 = int(input("Numero 1: "))
n2 = int(input("Numero 2: "))
n3 = int(input("Numero 3: "))

if n1 > n2 and n1 > n3:
    print(f"{n1} É maior que {n2} e {n3}")
    
elif n2 > n1 and n2 > n3:
    print(f"{n2} É maior que {n1} e {n3}")
    
elif n3 > n1 and n3 > n2:
    print(f"{n3} É maior que {n1} e {n2}")
