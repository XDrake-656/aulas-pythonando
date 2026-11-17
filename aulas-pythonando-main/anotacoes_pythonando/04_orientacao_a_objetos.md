# 🧱 Módulo 04: Orientação a Objetos (POO) e Arquitetura

## Conceitos Base
* **Princípio DRY (*Don't Repeat Yourself*):** Evite repetir código; agrupe lógicas reutilizáveis em funções e classes.
* **Classe (`class`):** O molde (*blueprint*). Nomeada sempre em *PascalCase* segundo a PEP 8 (ex: `MinhaClasse`).
* **Objeto (Instância):** A entidade criada a partir do molde.

```python
class Person:
    especie = "Humano"  # Atributo de CLASSE (compartilhado por todos)

    def __init__(self, name: str, age: int):
        # Atributos de INSTÂNCIA (exclusivos de cada objeto)
        self.name = name
        self.age = age
```
* **`self`:** Referência à própria instância que está chamando o método.

---

## Métodos Especiais (Dunder / Magic Methods)
* Os métodos mágicos são métodos especiais cujos nomes começam e terminam com sublinhados duplos, como __init__() e __str__(). Por causa dos sublinhados duplos, eles também são chamados métodos de dunder

|      Método      |        Chamado por       | Descrição                                           |
| :--------------- | :----------------------- | :-------------------------------------------------- |
| `__init__()`     | `Person(...)`            | Construtor executado ao criar um novo objeto        |
| `__str__()`      | `print(obj)`, `str(obj)` | Representação em texto legível para o usuário final |
| `__repr__()`     | `repr(obj)`              | Representação técnica voltada para o desenvolvedor  |
| `__eq__()`       | `obj1 == obj2`           | Define como dois objetos são comparados             |
| `__add__()`      | `obj1 + obj2`            | Define o comportamento do operador `+`              |
| `__len__()`      | `len(obj)`               | Retorna o tamanho do objeto                         |
| `__lt__()`       | `obj1 < obj2`            | Define ordenação ("menor que")                      |
| `__contains__()` | `item in obj`            | Define o comportamento do operador `in`             |
| `__call__()`     | `obj(...)`               | Permite chamar o objeto como se fosse uma função    |

---

## Decoradores de Métodos (`@classmethod` e `@staticmethod`)
* **`@classmethod`:** Pertence à class em si, e não a uma instância individual.
>Como funciona: Recebe a própria classe como primeiro parâmetro, chamado por convenção de `cls`. É muito usado para criar construtores alternativos (*factory methods*).

* **`@staticmethod`:**Em Python, um método estático é um método que pertence a class mas não opera em uma instância ou na class em si.
> Os métodos estáticos não recebem uma resposta implícita auto ou argumento CLS. Isso significa que eles não podem acessar ou modificar atributos de instância ou atributos de classe.
> Usamos métodos estáticos para utilizar funções que logicamente pertencem a uma classe, mas não exigem acesso a nenhuma instância ou dados em nível de classe.

```python
class Person:
    current_year = 2026

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name: str, birth_year: int):
        """Recebe a classe (cls) e cria um construtor alternativo."""
        age = cls.current_year - birth_year
        return cls(name, age)

    @staticmethod
    def is_adult(age: int) -> bool:
        """Função utilitária: não acessa nem self nem cls."""
        return True if age >= 18 else False
```

---

## Arquitetura MVC (Model - View - Controller)
* **Model (Modelo):** Gerencia os dados, consultas ao banco de dados e regras de negócio. Não sabe como a tela funciona.
* **View (Visão):** Camada de apresentação e interface com o usuário. Exibe dados e captura ações.
* **Controller (Controlador):** Intermediário entre os dois. Recebe ações da *View*, aciona o *Model* e devolve o resultado para a *View* exibir.
