import datetime


class Category:
    def __init__(self,category):
        self.category = category

class Products:
    def __init__(self, name, price, category: Category):
        self.name = name
        self.price = price
        self.category = category

class Inventory:
    def __init__(self, product: Products, quantity):
        self.product = product
        self.quantity = quantity

class Sale:
    def __init__(self, itensSold: Products, saler, client, quantitySold, date: str | None = None):
        self.itensSold = itensSold
        self.saler = saler
        self.client = client
        self.quantitySold = quantitySold
        self.date = date if date is not None else datetime.now().strftime("%d/%m/%y")

class Supplier:
    def __init__(self, name, cnpj, businessPhone, category):
        self.name = name
        self.cnpj = cnpj
        self.businessPhone = businessPhone
        self.category = category

class Person:
    def __init__(self, name, number, cpf, email, addres):
        self.name = name
        self.number = number
        self.cpf = cpf
        self.email = email
        self.addres = addres

class Employee(Person):
    def __init__(self, clt, name, number, cpf, email, addres):
        self.clt = clt
        super().__init__(name, number, cpf, email, addres)
