# class Dog():
#     """ A simple dog class"""
#
#     def __init__(self, name, age):
#         """Initialize name and age attribute"""
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         """Dog sitting function"""
#         print(self.name.title() + " is now siting down.")
#
#     def roll_over(self):
#         """Dog rolling over function"""
#         print(self.name.title() + " is now rolling over.")
#
# my_dog = Dog('Bella', 11)
# your_dog = Dog('lucy', 7)
# print("Our dog's name is " + my_dog.name.title() + ".")
# print("Our dog is " + str(my_dog.age) + " years old.")
# my_dog.sit()
# my_dog.roll_over()
#
# print("\nYour dog's name is " + your_dog.name.title()+ "." + your_dog.name.title()+ "is " + str(your_dog.age) + "years old")
# your_dog.sit()
# your_dog.roll_over()

# 9.1 ( Reasturant)

class Restaurant():

    def __init__(self, restaurant_name, cusine_type):
        """ basic info about reasturnat"""
        self.name = restaurant_name
        self.type = cusine_type

    def describe_reasturant(self):
        """ Function that decribe reasturant"""
        print("The name of this special reasturnat is " + self.name.title() + ". And it's a " + self.type + " type of reasturant")

    def open_restaurant(self):
        """ Shows if the restaurant is open or not"""
        print("The restaurant is open 24/7/365")

restaurant_details = Restaurant("Lesu Mia's Restaurant", "Street food")
print("MY favorite restaurant is " + restaurant_details.name.title())
print("It a " + restaurant_details.type.title() + " type of restaurant")
restaurant_details.describe_reasturant()
restaurant_details.open_restaurant()

# 9.2 (Three Restaurant)
first_instance = Restaurant("Aangan", "South East Asian Food")
first_instance.describe_reasturant()

second_instance = Restaurant("In n out", "Fast ")
second_instance.describe_reasturant()

third_instance = Restaurant("Somethign", "something")
third_instance.describe_reasturant()

# 9.3(Users)

class User():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        """ Details about the user"""
        print("My first name is " + self.first_name + " and My last name is " + self.last_name)

    def greet_user(self):
        print("Hello Beautiful " + self.first_name + " "+  self.last_name)

user1 = User("Aktar", "Zaman")
user1.describe_user()
user1.greet_user()

# Car class
