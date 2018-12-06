from car import ElectricCar

# my_new_car = Car("Audi", "R8", 2016)
# print(my_new_car.get_desctiptive_name())
#
# # my_new_car.odometer_reading = -50
# my_new_car.read_odometer(-50)

my_tesla = ElectricCar("Tesla", "Model S", 2016)
print(my_tesla.get_desctiptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
