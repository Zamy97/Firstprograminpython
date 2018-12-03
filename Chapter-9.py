class Dog():
    """ A simple dog class"""

    def __init__(self, name, age):
        """Initialize name and age attribute"""
        self.name = name
        self.age = age

    def sit(self):
        """Dog sitting function"""
        print(self.name.title() + "is now siting down")

    def roll_over(self):
        """Dog rolling over function"""
        print(self.name.title() + "is now rolling over")

my_dog = Dog('Bella', 11)
print("Our dog's name is " + my_dog.name.title())
print("Our dog is " + str(my_dog.age) + " years old")
