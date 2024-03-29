"""
staticmethod:
- an Klasse statt Objekt gebunden
- kann also aufgerufen werden, ohne ein Objekt zu erzeugen
- kann NICHT den inneren state eines Objekts ändern
- keine Referenz mit self, wie wir es von Methoden innerhalb von Klassen gewohnt sind
- verwendet man oft für sog. utility methods, die nicht an den Lifecycle eines Objekts
gebunden sind

classmethod:
- ähnlich wie staticmethod verbunden mit der Klasse selbst nicht mit einem Objekt
- kein self, also Objektreferenz, aber dafür eine Klassenreferenz
- kann auch von einem Objekt aufgerufen werden, anders als staticmethod
- wird als alternativer Konstruktor häufig verwendet
- starten dann oft mit "from_ ..."
"""
from datetime import date


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_person(self):
        print(f"Mein Name ist {self.name} und ich bin {self.age} Jahre alt.")

    @classmethod
    def from_birthday(cls, name, birthday):
        return cls(name, date.today().year - birthday)
    


class Calculator:

    @staticmethod
    def addNumbers(x, y):
        return x + y

print('Product:', Calculator.addNumbers(15, 110))
