from model import Person


class PersonDal:
    @classmethod
    def save(cls, person: Person):
        with open('persons.txt', 'w') as arq:
            arq.write(person.name + " " + str(person.age) + " " + person.cpf)

    @classmethod
    def read(cls):
        name = "Davi"
        age = 25
        cpf = "34342553432"
        return Person(name, age, cpf)
