# A Simple Example of IF statememnt

# cars = ['audi', 'bmw', 'subaru', 'toyota']
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())


# Checking for inequality

# requested_topping = 'mushroom'
# if requested_topping != 'pencil':
#     print("hold the anchovies")

# Checking Whether a Value Is Not in a List

# banned_users = ['andrew', 'carolina', 'david']
# user = 'Marie'
#
# if user not in banned_users:
#     print(user.title() + ", you can do whatever you want")

# 5.1 (Conditional Test)

# car = 'subaru'
# print("Is car == 'subaru' ?? I predict subaru")
# print(car == 'subaru')
#
# animal = "monkey"
# print("Guess the animal? Is it monkey?")
# print(animal == "lion")
#
# is_passed = "passed"
# print("Do you think you passed the test? type Passed or failed?")
# print(is_passed == "passed")

#Just playing with the if statement
# hungry_input = input("Are you hungry? Yes or no?: ")
# if hungry_input == 'yes':
#     print("You need to go eat then.")
# else:
#     print("well then I am sorry for you!")

# thirsty = "yes"
# print("Are you thirsty? Want some water")
# print(thirsty == "no")
#
#
# own_a_car = "hell ya"
# print("Do you have your own car??")
# print(own_a_car == "hell ya")


# 5.2 (More conditional tests)
# No that important! just do something and move on!

# IF STATEMENT

# age = 12
#
# if age >= 18:
#     print("you are old enough to vote, now go select a good president for our future")
# else:
#     print("sorry you are too young to vote")



# Amusement park ticket test

age = 67

if age < 4:
    price = 0

elif age < 18:
    price = 5

elif age < 65:
    price = 10

else:
    price = 5

print("Your Admission ticket is $" + str(price) + ".")
