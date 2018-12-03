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

# class Restaurant():
#
#     def __init__(self, restaurant_name, cusine_type):
#         """ basic info about reasturnat"""
#         self.name = restaurant_name
#         self.type = cusine_type
#
#     def describe_reasturant(self):
#         """ Function that decribe reasturant"""
#         print("The name of this special reasturnat is " + self.name.title() + ". And it's a " + self.type + " type of reasturant")
#
#     def open_restaurant(self):
#         """ Shows if the restaurant is open or not"""
#         print("The restaurant is open 24/7/365")
#
# restaurant_details = Restaurant("Lesu Mia's Restaurant", "Street food")
# print("MY favorite restaurant is " + restaurant_details.name.title())
# print("It a " + restaurant_details.type.title() + " type of restaurant")
# restaurant_details.describe_reasturant()
# restaurant_details.open_restaurant()

# 9.2 (Three Restaurant)
# first_instance = Restaurant("Aangan", "South East Asian Food")
# first_instance.describe_reasturant()
#
# second_instance = Restaurant("In n out", "Fast ")
# second_instance.describe_reasturant()
#
# third_instance = Restaurant("Somethign", "something")
# third_instance.describe_reasturant()

# 9.3(Users)
#
# class User():
#
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def describe_user(self):
#         """ Details about the user"""
#         print("My first name is " + self.first_name + " and My last name is " + self.last_name)
#
#     def greet_user(self):
#         print("Hello Beautiful " + self.first_name + " "+  self.last_name)
#
# user1 = User("Aktar", "Zaman")
# user1.describe_user()
# user1.greet_user()

# Car class

class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model= model
        self.year = year
        self.odometer_reading = 0

    def get_desctiptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = str(self.year) + ' ' + self.make + ' '+self.model
        return long_name.title()

    def read_odometer(self):
        """print a statement showing the car's milege"""
        print("This car has " +str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        set the odometer reading to given valueself.

        Reject the change if it attempts to roll the odometer back.

        """

        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Cmo'n man! Y u trying to lie to me")

    def increment_odometer(self, miles):
        """add the given amount to the odometer"""
        if miles >= self.odometer_reading:
            self.odometer_reading += miles
        else:
            print("Get a life")

# my_new_car = Car('Scion', 'FRS', 2017)
# print(my_new_car.get_desctiptive_name())
# my_new_car.read_odometer()
#
# my_new_car.odometer_reading = 45
# # my_new_car.read_odometer()
#
# my_new_car.update_odometer(65)
# my_new_car.read_odometer()

my_used_car = Car("Subaru", "sports", 2013)
print(my_used_car.get_desctiptive_name())

my_used_car.update_odometer(17800)
my_used_car.read_odometer()

my_used_car.increment_odometer(-20000)
my_used_car.read_odometer()

# 9.4 (Number Served)
