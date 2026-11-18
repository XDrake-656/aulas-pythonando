# ruff: noqa: N999
from models import *  # noqa: I001

class DaoCategory:
    @classmethod
    def save(cls, category):
        with open('category.txt', 'a') as file:
            file.writelines(category)
            file.writelines('\n')

    @classmethod
    def read(cls):
        with open('category.txt', 'r') as file:
            cls.category = file.readlines()
        cls.category = [category.replace('\n', '') for category in cls.category]

        c = []
        for i in cls.category:
            c.append(Category(i))
        return c

class DaoSale:
    @classmethod
    def save(cls, sale: Sale):
        with open('sale.txt', 'a') as file:
            file.writelines(sale.itensSold.name + "|" + str(sale.itensSold.price) + "|" + sale.itensSold.category + "|" + sale.saler + "|" + sale.client + "|" + str(sale.quantitySold) + "|" + sale.date)
            file.writelines('\n')

    @classmethod
    def read(cls):
        with open('sale.txt', 'r') as file:
            cls.sale =file.readlines()
        cls.sale = [sale.replace('\n', '') for sale in cls.sale]
        cls.sale = [sale.split('|') for sale in cls.sale]
        v = []
        for i in cls.sale:
            v.append(Sale(Products(i[0], i[1], i[2]),i[3], i[4], i[5], i[6]))
        return v
