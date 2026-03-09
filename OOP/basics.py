# Creating first class
# pass - it means they have no value yet
class People:
    # __init__ is the constructor from class People
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_information(self):
        print(f"Hello, I'm {self.name} and I'm {self.age} years old!")

people1 = People("Max", 18) # now, people1 is an object from class People
people1.show_information()
