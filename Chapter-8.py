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

def make_album(artist_name, album_title):
    artist_info = {
        'artist name':artist_name,
        'artist album':album_title
        }
    return artist_info

first_artist = make_album("Cardi B", "Invasion of privacy",)
print(first_artist)

second_artist = make_album("J cole","Jumping")
print(second_artist)

third_album = make_album("Aktar","Help Immigrants")
print(third_album)

# make albums with tracks

def album_with_tracks(name_artist,album_name, tracks = ""):
    info_artist = {
        'artist name': name_artist,
        'artist album':album_name,
        }
    if tracks:
        info_artist['tracks'] = tracks
    return info_artist

info = album_with_tracks("Fariha","jingo",9)
print(info)
