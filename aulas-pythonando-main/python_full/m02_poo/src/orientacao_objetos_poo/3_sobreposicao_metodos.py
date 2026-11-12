class Person:
    def __init__(self, name, cpf):
        self.name = name
        self.cpf = cpf

class Seller(Person):
    def __init__(self, id_seller, name, cpf):
        super().__init__(name, cpf)
        self.id_seller = id_seller

class Customer(Person):
    def __init__(self, id_customer, name, cpf):
        super().__init__(name, cpf)
        self.id_customer = id_customer
        
s1 = Seller(1, "Caio", 52562455)
c1 = Customer(2, "Davi", 85696392)

print(s1.id_seller)
print(s1.name)
print(s1.cpf)
print("=" * 10)
print(c1.id_customer)
print(c1.name)
print(c1.cpf)
