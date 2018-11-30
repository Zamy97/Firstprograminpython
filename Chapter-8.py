import printing_models
from printing_models import display_message
from printing_models import display_message as message
import printing_models as testing
from printing_models import *
# A Simple function
# def greet_user(username):
#     """Display a simple greeeting."""
#     print("Hello "+ username.title()+ "!")
#
# greet_user("Aktar")


# 8.1 (Message)
# def display_message():
#     print("I am learning about functions in this chapter because I am not comfortable with how to write them so I want to learn it in this chapter and be good at it! Uk wt m sayinn")
#
# display_message()

# 8.2 (Favorite book)

# def favorite_book(title):
#     print("One of my favorite book is :" + title.title())
#
# favorite_book(" If Beale Street could talk")



# POsitional function

# def describe_pet(pet_name,animal_type = "Cat"):
#     """Display information about a pet"""
#     print("I have a "+animal_type.title()+".")
#     print("My " + animal_type.title() + "'s name is " +pet_name + ".")
#
# describe_pet("Goru")
# describe_pet("leina",animal_type = "Horse",)
# # A dog named Willie.
# describe_pet('willie')
# describe_pet(pet_name='willie')
# # A hamster named Harry.
# describe_pet('harry', 'hamster')
# describe_pet(pet_name='harry', animal_type='hamster')
# describe_pet(animal_type='hamster', pet_name='harry')


# 8.3(T-Shirts)

# def make_shirts(shirt_size,message_on_shirt):
#     print("You ordered a " + shirt_size.upper() + " size shirt. And the message it's going to have is: "+ message_on_shirt.title())
#
# make_shirts("M","Sky is the limit.")
# make_shirts(message_on_shirt = "If they can do it, I can do it too!",shirt_size = "M")

# 8.4(Large Shirts)

# def make_shirts_here(shirt_size = "L",message_on_the_shirt = "I love Python."):
#     print("You order a " + shirt_size.upper() + " size shirt. And the message on the shirt will be: " + message_on_the_shirt)
#
# make_shirts_here()
# make_shirts_here("M")

# 8.5 (cities)

# def describe_cities(city_name,country_name = "Bangladesh."):
#     print(city_name.title() + " city is located in " + country_name.title())
#
#
# describe_cities("Sylhet")
# describe_cities("Berlin")
# describe_cities("Dhaka")


# Returning a simple value

# def get_formatted_name(first_name,last_name):
#     '''Return a full name, neatly formatted'''
#     full_name = first_name + " " + last_name
#     return full_name.title()
#
# her_full_name = get_formatted_name("Fariha","Zaman.")
# print(her_full_name)


# Making an argument optional

# def get_full_name(first_name, last_name, middle_name=""):
#     '''Return full name clearly"'''
#     if middle_name:
#         full_name = first_name + " " + middle_name + " " +last_name
#     else:
#         full_name = first_name + " " + last_name
#     return full_name.title()
#
# my_full_name = get_full_name("Aktar","Zaman")
# print(my_full_name)
# my_full_name = get_full_name("Aktar","Zaman","Uz")
# print(my_full_name)

# Build a person

# def build_person(first_name,last_name):
#     '''return a dictionary of information about a person'''
#     person = {
#         'first':first_name,
#         'last':last_name
#         }
#     return person
#
# full_name = build_person("Fariha","Zaman")
# print(full_name)

# making a person and their details

# def person_details(first_name,last_name,age=""):
#
#     person = {
#         'first':first_name,
#         'last':last_name
#         }
#     if age:
#         person['age'] = age
#     return person
# persons_name = person_details("Aktar","Zaman",21)
# print(persons_name)

# Function with a while Loop on page - 145

# def get_formatted_name(first_name,last_name):
#     full_name = first_name + ' ' + last_name
#     return full_name
#
#     # This is an infinite loop
# while True:
#     print("Enter q at any time to quit the program!")
#     f_name = input("What is your first name: ")
#     if f_name == 'q':
#         break
#
#     l_name = input("What's your last name: ")
#     if l_name == 'q':
#         break
#
#     asta_nam = get_formatted_name(f_name,l_name)
#     print("\nHello, "+ asta_nam + "!")
#     break

# 8.6 (City Names)

# def city_country(city_name,country_name):
#     city_and_country = city_name + " " + country_name
#
#     return city_and_country
#
# while True:
#     print("Tell me a name of a city and which country and i'll put it together for you lol!")
#     print("You can exit the program by entering q")
#
#     city_name_input = input("Type a city name: ")
#     if city_name_input == 'q':
#         break
#
#     country_name_input = input("Which country is that in: ")
#     if country_name_input == 'q':
#         break
#
#     name_of_the_city_and_country = city_country(city_name_input,country_name_input)
#     print("\n"+ city_name_input.title() + " is located in " + country_name_input.title() + "!")
#     exit()


# 8.7 (Album)

# def make_album(artist_name, album_title):
#     artist_info = {
#         'artist name':artist_name,
#         'artist album':album_title
#         }
#     return artist_info
#
# first_artist = make_album("Cardi B", "Invasion of privacy",)
# print(first_artist)
#
# second_artist = make_album("J cole","Jumping")
# print(second_artist)
#
# third_album = make_album("Aktar","Help Immigrants")
# print(third_album)
#
# # make albums with tracks
#
# def album_with_tracks(name_artist,album_name, tracks = ""):
#     info_artist = {
#         'artist name': name_artist,
#         'artist album':album_name,
#         }
#     if tracks:
#         info_artist['tracks'] = tracks
#     return info_artist
#
# info = album_with_tracks("Fariha","jingo",9)
# print(info)

# 8.8 (User albums)

# def user_name_album(singer_name, album_name):
#     user_input_artist_info = singer_name + " " + album_name
#
#     return user_input_artist_info
#
# while True:
#     print("you can exit the program by entering q")
#     artist_name_input = input("Who is your favorite artist? ")
#     if artist_name_input == 'q':
#         quit()
#
#     album_name_input = input("What's your favorite album of " + artist_name_input.title() +": ")
#     if album_name_input == 'q':
#         quit()
#
#     info_of_artist = user_name_album(artist_name_input,album_name_input)
#     print( "Your favorite artist is " + artist_name_input + ", and you love " + artist_name_input.title() + "'s"+ album_name_input + " album much.")
#     break
#


# Passing a list to a function




# def greet_users(names):
#     """ print a simple greeting to each user in the list"""
#     for name in names:
#         msg = " Hello, " + name.title() + "!"
#         print(msg)
# usernames = ["Aktar", "Fariha", "Tasnima"]
# greet_users(usernames)
#


# Modifying the list in a function

# def print_models(unprinted_designs, completed_models):
#     """
#      Simulate printing each design, until none are left.
#      Move each design to completed_models after printing.
#     """
#
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#
#         # Simulate creating a 3d print from the design.
#         print("Printing model: " + current_design)
#         completed_models.append(current_design)
#
# def show_completed_models(completed_models):
#     """Show all the models that were printed"""
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)
#
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []
#
# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)

# 8.9 (Magicians)

# def show_magician(magician_names):
#     """Print the name of each magician in the list."""
#     for magician_name in magician_names:
#         print("Hello, "+ magician_name + "!")

# magician_names = ["Fariha", "Aktar", "Bushra", "Tasnima", "Tamim", "Aminul"]
# show_magician(magician_names)

# def make_great(magician_names):
#     """Add 'the Great!' to each magician's name."""
#     great_magicians = []
#
#     # Make each magician great, and add it to great_magicians.
#     while magician_names:
#         magician = magician_names.pop()
#         great_magician = magician + ' You are amazing'
#         great_magicians.append(great_magician)
#
#     # Add the great magicians back into magicians.
#     for great_magician in great_magicians:
#         magician_names.append(great_magician)
#
#     return magician_names
#
# magician_names = ["Fariha", "Aktar", "Bushra", "Tasnima", "Tamim", "Aminul"]
# show_magician(magician_names)
# print("\n")
#
# # Magicians with the greeting
# make_great(magician_names)
#
# print("\n The original magician names")
# show_magician(magician_names)


# 8.11

# def show_magicians(magicians):
#     """Print the name of each magician in the list."""
#     for magician in magicians:
#         print(magician)
#
# def make_great(magicians):
#     """Add 'the Great!' to each magician's name."""
#     # Build a new list to hold the great musicians.
#     great_magicians = []
#
#     # Make each magician great, and add it to great_magicians.
#     while magicians:
#         magician = magicians.pop()
#         great_magician = magician + ' the Great'
#         great_magicians.append(great_magician)
#
#     # Add the great magicians back into magicians.
#     for great_magician in great_magicians:
#         magicians.append(great_magician)
#
#     return magicians
#
# magicians = ['Harry Houdini', 'David Blaine', 'Teller']
# show_magicians(magicians)
#
# print("\nGreat magicians:")
# great_magicians = make_great(magicians[:])
# show_magicians(great_magicians)
#
# print("\nOriginal magicians:")
# show_magicians(magicians)

# Passing an arbtriry number of arguments in your function

# def make_pizza(*toppings):
#     """print the list of toppings that have been requested"""
#     print(toppings)
#
# make_pizza("Mushrooms")
# make_pizza("Cheese", "green Peppers", "extra cheese")

# Making a pizza

# def make_pizza(*toppings):
#     """Summerize the pizza we are making"""
#     print("\n Making a pizza with the following toppings: ")
#     for topping in toppings:
#         print("- " + topping)
# make_pizza("Mushrooms")
# make_pizza("Cheese", "green Peppers", "extra cheese")

# passing in different types of parameters in your function

# def making_pizza(size, *toppings):
#
#     print("\nMaking a " + str(size) +
#             "-inch pizza with the following toppings:")
#     for topping in toppings:
#         print("- " + topping)
#
#
# making_pizza(16, "mushrooms")
# making_pizza(12, 'mushrooms', 'green peppers','extra cheese')

# 8.15 (Printing Models)
# Imported a file at the very top of this file

# 8.16(Different imports)

# Using the entire module import
# printing_models.greet_user("Fariha")

#importing functions from a module
# display_message()
# import function as an aias meaning that importing function as a certain name
# message()
# import the whole module as an alias
testing.display_message()
# importing all the function from the module
favorite_book("Python Crash Course")
