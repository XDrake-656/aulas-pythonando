class Person:
    def __init__(self, name, age, cpf):
        self.name = name
        self.age = age
        self.cpf = cpf
    def greet(self):
            print(f"Hello, my name is {self.name}")

# Create an object
p1 = Person("John", 36, 14536478)
p2 = Person("Davi Barros", 25, 18478277)
# Call the greet method
p1.greet()
p2.greet()
