# A Simple Example of IF statememnt

# cars = ['audi', 'bmw', 'subaru', 'toyota']
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())


# Checking for inequality

requested_topping = 'mushroom'
if requested_topping != 'pencil':
    print("hold the anchovies")

# Checking Whether a Value Is Not in a List

banned_users = ['andrew', 'carolina', 'david']
user = 'andrew'

if user not in banned_users:
    print(user.title() + ", you can do whatever you want")
