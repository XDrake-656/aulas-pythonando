class Person:
    lastname = "Barros"
    current_year = 2026
    def __init__(self, name, age, cpf):
        self.name = name
        self.age = age
        self.cpf = cpf
    def greet(self):
            print(f"Hello, my name is {self.name}")
    
    @classmethod
    def for_birth_year(cls, name, birth_year, cpf):
        age = cls.current_year - birth_year
        return cls(name, age, cpf)
    
    @staticmethod
    def is_adult(age):
        return True if age > 18 else False  # noqa: SIM210

p1 = Person("John", 36, 14536478)
p2 = Person("Davi", 25, 18478277)

Person.lastname = "Ronaldo"
print(p1.lastname)
print(p2.lastname)

p1.lastname = "Alonso"
print(p1.lastname)
print(p2.lastname)

p1.greet()
p2.greet()

p3 = Person.for_birth_year("Caio",2000, 34673686)
print(p3.age)
print(Person.is_adult(p3.age))
