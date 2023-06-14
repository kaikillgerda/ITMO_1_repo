class Mammal:
    className = 'Млекопитающее' #атрибут класса

class Dog(Mammal):
    species = 'Canis lupus' #атрибут класса

dog = Dog()
print(dog.className)