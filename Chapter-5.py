# A Simple Example of IF statememnt

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


# Checking for inequality

requested_topping = 'mushroom'
if requested_topping != 'pencil':
    print("hold the anchovies")

# Checking Whether a Value Is Not in a List

banned_users = ['andrew', 'carolina', 'david']
user = 'Marie'

if user not in banned_users:
    print(user.title() + ", you can do whatever you want")

# 5.1 (Conditional Test)

car = 'subaru'
print("Is car == 'subaru' ?? I predict subaru")
print(car == 'subaru')

animal = "monkey"
print("Guess the animal? Is it monkey?")
print(animal == "lion")

is_passed = "passed"
print("Do you think you passed the test? type Passed or failed?")
print(is_passed == "passed")

#Just playing with the if statement
hungry_input = input("Are you hungry? Yes or no?: ")
if hungry_input == 'yes':
    print("You need to go eat then.")
else:
    print("well then I am sorry for you!")

thirsty = "yes"
print("Are you thirsty? Want some water")
print(thirsty == "no")


own_a_car = "hell ya"
print("Do you have your own car??")
print(own_a_car == "hell ya")


# 5.2 (More conditional tests)
# No that important! just do something and move on!

# IF STATEMENT

age = 12

if age >= 18:
    print("you are old enough to vote, now go select a good president for our future")
else:
    print("sorry you are too young to vote")



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

print(" \nYour Admission ticket is $" + str(price) + ".")




# Pizzaria example

requested_topping = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_topping:
    print("Don't forget to add mushrooms on the pizza")
if 'pepperoni' in requested_topping:
    print("Don't forget on add pepperoni")
if 'extra cheese' in requested_topping:
    print("I'll make sure to add some extra cheese for you")

print("\nFinished making your pizza!")



# 5.3 (Alien Colors-1)

alien_color = "Red"
if alien_color is "Green":
    print("You earned 5 points")
elif alien_color is "Red":
    print("You get 5 points.")
elif alien_color is "Brown":
    print("you get 5 points")

# Version that doesn't pass the condition at all!

different_alien_color = "Brown"
if different_alien_color is "Pink":
    print("You get 5 points")
elif different_alien_color is "Blacl":
    print(" You get 5 points")
elif different_alien_color is "White":
    print("You get 5 points")


# 5.4 (Alien Color-2)

alien_colors = "Green"

if alien_colors is "Blue":
    print("you just earned 5 points for shooting the alien")
else:
    print("you just earned 10 points for nothing lol")


# 5.5 (Alien Color-3 using if-elif-else)

first_alien_color = "Blue"

if first_alien_color is "Green":
    print("Good job! You just earned 5 points")
elif first_alien_color is "Blue":
    print("You just earned 10 points")
elif first_alien_color is "Red":
    print("you just earned 15 points")


second_alien_color = "Green"

if second_alien_color is "Green":
    print("you just earned 5 points")
elif second_alien_color is "Red":
    print("You just earned 15 points")
elif second_alien_color is "Blue":
    pritn("you just earned 10 points")


third_alien_color = "Red"

if third_alien_color is "Red":
    print("you just earned 15 points")
elif third_alien_color is "Green":
    print("you don't get anything")
elif third_alien_color is "Blue":
    print("just go home man")


# 5.6 (Stages of life)

persons_age = 65

if persons_age <= 2:
    print(" You are just a baby still!")
elif persons_age < 13:
    print("You are a kid bro")
elif persons_age < 20:
    print("You are a teenager! Make Sure you focus on your school")
elif persons_age < 65:
    print("you are an adult. Get your life together")
elif persons_age >= 65:
    print("Have you enjoyed your life thus far?")

# 5.7 (Favorite Fruit)

my_favorite_fruits = ["Mango","Lichi","Tomato","Lemon","Straberry"]

if "Mango" in my_favorite_fruits:
    print("Dmn man you love mangoes")
if "Banana" in my_favorite_fruits:
    print("Do you like Banana this much?")
if "Tomato" in my_favorite_fruits:
    print("you seem to love Tomato")
if "Lemon" in my_favorite_fruits:
    print("Make some lemon juice with Lemon")


# Checking if the list is empty

requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("adding" + requested_topping + ".")
else:
    print("Do you want plain pizza?")


#USING MULTIPLE LISTS

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry we don't have " + requested_topping + ".")


# 5.8 (Hello Admin) + 5.9 (No users)

usernames = ["Zamy97","admin","Fariha_Zaman","Bushra31","Tasnima_21"]

if usernames:
    for user in usernames:
        if user == "admin":
            print("Hello Admin! Would you like to see a status report?")
        else:
            print("Hello " + user + "! Thank you for logging back in again")
else:
    print(" We need more users! ")




#Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).

number_list = []

for every_number in range(1500, 2701):
    if every_number%7 == 0 and every_number%5 == 0:
        number_list.append(every_number)
print(number_list)


# 5.10 (Checking Usernames)

current_users = ["Bushra31","Fariha18","ZyanUK","Shakib75","Tamim99"]
new_users = ["Attractive", "Fariha18","Bristle", "Attractive","Sing","Bobourusis","Shakib75","BootTips"]

current_user_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_user_lower:
        print("That "+ new_user + " name has been taken unfortunately! Choose another username pleas!")
    else:
        print("This username is available")


# 5.11 (Ordinal Numbers)

number_list = list(range(1,10))

for single_number in number_list:
    if single_number <= 1:
        print(str(single_number) + " st")
    elif single_number <= 3:
        print(str(single_number) + " rd")
    else:
        print(str(single_number) + " th")
