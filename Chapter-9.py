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

9.2 (Three Restaurant)
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

my_new_car = Car('Scion', 'FRS', 2017)
print(my_new_car.get_desctiptive_name())
my_new_car.read_odometer()

my_new_car.odometer_reading = 45
# my_new_car.read_odometer()

my_new_car.update_odometer(65)
my_new_car.read_odometer()

my_used_car = Car("Subaru", "sports", 2013)
print(my_used_car.get_desctiptive_name())

my_used_car.update_odometer(17800)
my_used_car.read_odometer()

my_used_car.increment_odometer(-20000)
my_used_car.read_odometer()

# 9.4 (Number Served)

class Restaurant():

    def __init__(self, restaurant_name, cusine_type):
        """ basic info about reasturnat"""
        self.name = restaurant_name
        self.type = cusine_type
        self.number_served = 0

    def describe_reasturant(self):
        """ Function that decribe reasturant"""
        print("The name of this special reasturnat is " + self.name.title() + ". And it's a " + self.type + " type of reasturant")

    def open_restaurant(self):
        """ Shows if the restaurant is open or not"""
        print("The restaurant is open 24/7/365")

    def set_number(self, number):
        """let's you set a number of people is being served"""
        self.number_served = number
    def increment_number(self, number):
        if number >= self.number_served:
            self.number_served += number
        else:
            print("Type a bigger number")

restaurant_details = Restaurant("Lesu Mia's Restaurant", "Street food")
print(restaurant_details.name + " has served about " + str(restaurant_details.number_served) + " People")
restaurant_details.number_served = 500
print(restaurant_details.name + " has served about " + str(restaurant_details.number_served) + " People")

restaurant_details.set_number(9)
print(restaurant_details.name + " has served about " + str(restaurant_details.number_served) + " People")

restaurant_details.increment_number(499)
print(restaurant_details.name + " has served about " + str(restaurant_details.number_served) + " People")

# 9.5 (Login Attemps)

# class User():
#
#     def __init__(self, first_name, last_name, login_attempts):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.login_attempts = login_attempts
#
#     def describe_user(self):
#         """ Details about the user"""
#         print("My first name is " + self.first_name + " and My last name is " + self.last_name)
#
#     def greet_user(self):
#         print("Hello Beautiful " + self.first_name + " "+  self.last_name)
#     def increment_login_attempts(self):
#         self.login_attempts += 1
#     def reset_login_attemps(self):
#         self.login_attempts = 0
#
# user1 = User("Aktar", "Zaman", 5)
# user1.describe_user()
# user1.greet_user()
# user1.increment_login_attempts()
# user1.increment_login_attempts()
# user1.increment_login_attempts()
# user1.increment_login_attempts()
# user1.increment_login_attempts()
# user1.increment_login_attempts()
# user1.increment_login_attempts()
# user1.increment_login_attempts()
# # user1.reset_login_attemps()
#
# print(user1.login_attempts)

# Battery class

class Battery():

    def __init__(self, battery_size = 70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print a statement about the rance this battery provides"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go appropriately "+ str(range)
        message += " miles on a full change"
        print(message)



class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class"""
        super().__init__(make, model, year)
        self.battery = Battery(85)

    # def describe_battery(self):
    #     """Print a statement describing the battery size."""
    #     print(self.make +" "+ self.model.title() + " has a " + str(self.battery_size) + "-kWh battery.")


my_tesla = ElectricCar("Tesla", "model s", 2016)
print(my_tesla.get_desctiptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


# 9.6 ( Ice Cream Stand )

class IceCreamStand(Restaurant):

    def __init__(self, name, cusine_type="ice_cream"):
        super().__init__(name, cusine_type="ice_cream")
        self.flavors = []

    def show_flavors(self):
        print("\n Here's the following type of flavors " + self.name + " has: ")
        for flavor in self.flavors:
            print("- "+flavor.title())

ice_cream_instance = IceCreamStand("Andrew's Ice-Cream")
ice_cream_instance.flavors = ['vanilla', 'chocolate', 'black cherry']

ice_cream_instance.describe_reasturant()
ice_cream_instance.show_flavors()


# 9.7 ( Admin )

class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Display a summary of the user's information."""
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print("\nWelcome back, " + self.username + "!")

    def increment_login_attempts(self):
        """Increment the value of login_attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login_attempts to 0."""
        self.login_attempts = 0


class Admin(User):
    """A user with administrative privileges."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the admin."""
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = []
        self.privilege = privileges('can reset passwords',)

    def show_privileges(self):
        """Display the privileges this administrator has."""
        print("\nPrivileges:")
        for privilege in self.privileges:
            print("- " + privilege)


eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()

eric.privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]

eric.show_privileges()

# 9.8 (  privileges )

class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Display a summary of the user's information."""
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print("\nWelcome back, " + self.username + "!")

    def increment_login_attempts(self):
        """Increment the value of login_attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login_attempts to 0."""
        self.login_attempts = 0


class Admin(User):
    """A user with administrative privileges."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the admin."""
        super().__init__(first_name, last_name, username, email, location)

        # Initialize an empty set of privileges.
        self.privileges = Privileges()

class Privileges():
    """A class to store an admin's privileges."""

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print("- " + privilege)
        else:
            print("- This user has no privileges.")


eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()

eric.privileges.show_privileges()

print("\nAdding privileges...")
eric_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
eric.privileges.privileges = eric_privileges
eric.privileges.show_privileges()

# 9.9 (Battry Upgrade) [Will do it later]
# 9.10
