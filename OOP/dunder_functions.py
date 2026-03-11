# Underscore Functions (or dunder functions) are special methods from OOP in Python

class Person():
    # Class constructor to create new Person objects
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Official representation (usually used to debbug variables)
    def __repr__(self):
        return f"Person name: {self.name}"
    
    # Friendly representation
    def __str__(self):
        return f"Hello, I'm {self.name}"
    
    # Equals verification (age)
    def __eq__(self, other):
        return self.age == other.age
    
    # To sum attributes (example age)
    def __add__(self, other):
        return self.age + other.age
    
    # Less than
    def __lt__(self, other):
        return self.age < other.age
    
    # Bool funcion, used in if conditions
    def __bool__(self):
        return self.age >= 18
    
    # Lenght for atributte
    def __len__(self):
        return f"{len(self.name)} letters"
    
    # Contains something
    def __contains__(self, letter):
        return letter in self.name
    
# Creating objects
person1 = Person("Jhon", 18)
person2 = Person("Joshua", 20)

# Printing
print("="*15)
print("Some examples")
print("="*15)
print(f"Firt Person:\n{person1.__repr__()}\n{person1.__str__()}\n")
print(f"Second Person:\n{person2.__repr__()}\n{person2.__str__()}\n")
print(f"Are the names equals?\n{person1.__eq__(person2)}\n")
print(f"Ages sum\n{person1.__add__(person2)}\n")
print(f"Is the youngest person Person1?\n{person1.__lt__(person2)}\n")
print(f"Is Person1 an Adult?\n{person1.__bool__()}\n")
print(f"How many letters are in Person 2's name?\n{person2.__len__()}\n")
print(f"Contains Person2's name letter I?\n{person2.__contains__("I")}\n")

# Other tests
print(person1)  # Call __str__ method
print(person1 == person2)   # Call __eq__ method
