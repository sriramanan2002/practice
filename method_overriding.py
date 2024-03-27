#Python program for method overriding

class Animal:
    def eat(self):
        return "This animal eats food!"

class cat(Animal):
    def eat(self):
        return "Cat eats fishes!"

generic_animal = Animal()
print(generic_animal.eat())  # Calling animal class commonly the O/P will be "This animal eats food"

specific_animal = cat()
print(specific_animal.eat())    # Calling animal class inside cat class the O/P will be Cat eats fishes






















