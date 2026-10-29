class Person: #criar uma classe
    
    def walk(self):
        print("I'm walking")
    def talk(self):
        print("I'm talking")
        
class Customer(Person): #criar uma classe com a erance de outra classe
    
    def buy(self):
        print("I'm buying")

class Seller(Person):
    
    def sell(self):
        print("I'm selling")

s1 = Seller()
c1 = Customer()

s1.walk()
s1.talk()
s1.sell()

c1.walk()
c1.talk()
c1.buy()
