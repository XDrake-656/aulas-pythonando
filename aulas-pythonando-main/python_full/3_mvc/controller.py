from dal import PersonDal
from model import Person


class PersonController:
    @classmethod
    def sing_up(cls, name, age, cpf):
        if len(name) > 2 and (age > 0 and age < 110) and len(cpf) == 11:
            try:
                PersonDal.save(Person(name, age, cpf))
                return True
            except:  # noqa: E722
                return False
        else:
            return False
