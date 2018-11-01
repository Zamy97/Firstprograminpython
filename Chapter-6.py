# A simple Dictionary

# alien_0 = {'color': 'Green', 'point':5}
#
# print(alien_0['color'])
# print(alien_0['point'])

#Alien Shoot down

# alien_1 = {'color': 'green', 'points': 5}
# new_points = alien_1['points']
# print("You just earned " + str(new_points)+ " points.")


# Adding a new Key-Value pairs

# alien_2 = {'color': 'green', 'points': 5}
# print(alien_2)
#
# alien_2['X-position'] = 0
# alien_2['y-position'] = 25
# print(alien_2)


# Starting with an empty Dictionary
# Modifying Values in a Dictionary

# alien_3 = {}
# alien_3['color'] = 'Blue'
# alien_3['points'] = 233
# print(alien_3)
#
# alien_3['color'] = 'Yellow'
# print(alien_3)


# Tracking Alien's Movement

# alien_4 = {'x-position': 0, 'y-position': 25, 'speed':'medium'}
# print("Original x-position: " + str(alien_4['x-position']))


# Move the Alien to the right
#Determine how far to move the alien based on it's current speed'
# if alien_4['speed'] == 'slow':
#     x_increment = 1
# elif alien_4['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3
#
# # The new position is the old position plus the increment.
# alien_4['x_position'] = alien_4['x_position'] + x_increment
#
# print("New x-position: " + str(alien_4['x_position']))




# Remove from the dictionary
# alien_5 = {'color': 'Blue', 'points':10}
# print(alien_5)
#
# del alien_5['points']
# print(alien_5)
#
#
# favorite_languages = {'jen':'python','sarah':'c','edward':'euby','aktar':'python',}
# print("Sarah's favorite language is " + favorite_languages['sarah'].title() + ".")
# print("Aktar's favorite language is " + favorite_languages['aktar'].title() + ".")


# 6.1 (Person)

# my_favorite_person = {'first_name':'Fariha','last_name':'Zaman','age':18,'city':'Warren','state':'Michigan.'}
# print("My favorite person's name is " + my_favorite_person['first_name'] +  my_favorite_person['last_name'] + ". She is "+ str(my_favorite_person['age']) + " years old. she lives in "+my_favorite_person['city']+ "," + my_favorite_person['state'])

# 6.2 (Favorite Numbers)

# favorite_number = {'Andrew':8, 'Aktar':19,'Andrea':25,'Ashraf':94,'Bushra':15}
# print("Andrew's Favorite number is " + str(favorite_number['Andrew']) +  ". Aktar's favorite number is " + str(favorite_number['Aktar']) + ". Andrea's favorite number is " + str(favorite_number['Andrea']))

# 6.3 (Glossary)

# glossary = {
#     'string': 'A series of characters.',
#     'comment': 'A note in a program that the Python interpreter ignores.',
#     'list': 'A collection of items in a particular order.',
#     'loop': 'Work through a collection of items, one at a time.',
#     'dictionary': "A collection of key-value pairs.",
#     }
#
#
# word = 'string'
# print("\n" + word.title() + ": " + glossary[word])
#
# word = 'comment'
# print("\n" + word.title() + ": " + glossary[word])
#
# word = 'list'
# print("\n" + word.title() + ": " + glossary[word])
#
# word = 'loop'
# print("\n" + word.title() + ": " + glossary[word])
#
# word = 'dictionary'
# print("\n" + word.title() + ": " + glossary[word])

# Looping through a dictionary

# user_0 = {
#     'username': 'fariha18',
#     'first_name': 'Fariha',
#     'last_name': 'Zaman',
#     }
# for key, value in user_0.items():
#     print("\nKey: " + key)
#     print("value: " + value)

# Looping through a dictionary

# favorite_languages = {
#        'jen': 'python',
#        'sarah': 'c',
#        'edward': 'ruby',
#        'phil': 'python',
#        }
#
# for name, language in favorite_languages.items():
#     print(name.title() + "'s favorite language is " + language.title()+ ".")
#
# for name in favorite_languages.keys():
#     print(name.title())

# Printing a message to a friend about their favorite programming language


# favorite_languages = {
#        'jen': 'python',
#        'sarah': 'c',
#        'edward': 'ruby',
#        'phil': 'python',
#        }
# friends = ['phil','sarah']
# for name in sorted(favorite_languages.keys()):
#     print(name.title())
#
#     if name in friends:
#         print(" Hi " + name.title() + ", I see you love " +favorite_languages[name].title()+ "!")
#
# if 'Erin' not in favorite_languages.keys():
#     print(" HI Erin, please take our survey")


# Looping Through All Values in a Dictionary

# for language in set(sorted(favorite_languages.values())):
#     print(language.title())


# 6.4 (Glossary-2)

# glossary_1 = {
#      'string': "A series of characters.",
#      'comment': "A note in a program that the Python interpreter ignores.",
#      'list': "A collection of items in a particular order.",
#      'loop': "Work through a collection of items, one at a time.",
#      'dictionary': "A collection of key-value pairs.",
#      'built in function': "sometimes your best friedn would be the built in function"
#      }
#
# for concept, description in glossary_1.items():
#     print("\n" + concept.title()+ ": " + description.title())


# 6.5 (Rivers)

# rivers = {
#     'nile':'egypt',
#     'surma':'sylhet',
#     'burigonga':'Dhaka',
#     }
#
# for river, location in sorted(rivers.items()):
#     print(river.title() + ": River run though "+ location.title() + ".")
#
#
# for river in rivers.keys():
#     print(river)
#
# for location in rivers.values():
#     print(location)

# 6.6 (Polling)

# favorite_languages = {
#        'jen': 'python',
#        'sarah': 'c',
#        'edward': 'ruby',
#        'phil': 'python',
#        'fariha':'swift',
#        'Bushra':'C++',
#        'Tamim':'Java'
#        }
#
#
# friends_to_take_polls= ['Andrea','Andrew','Fang','faith','fariha','Tamim']
#
# for name in sorted(favorite_languages.keys()):
#     # print(name.title())
#
#     if name in sorted(friends_to_take_polls):
#         print( "\n" + name.title() + ", Thank you for taking the poll! You are the best!")
#     else:
#         print("\n"+name.title()+ ", Could you please take the poll")


# A list of dictionaries

# alien_6 = {'color':'green','points': 5}
# alien_7 = {'color':'blue','points': 10}
# alien_8 = {'color':'yellow','points': 15}
#
# aliens = [alien_6, alien_7,alien_8]
#
# for alien in aliens:
#     print(alien)


# Make an empty list for sorting aliens.
aliens = []

# Make 30 green aliens
# for alien in range(30):
#     new_alien = {'color': 'yellow', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)
#
# for alien in aliens[0:5]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['points'] = 25
#         alien['speed'] = 'medium'
#     elif alien['color'] == 'yellow':
#         alien['color'] = 'red'
#         alien['points'] = 50
#         alien['speed'] = 'fast'
#
# # SHow the first 5 aliens
# for alien in aliens[:10]:
#     print(alien)
#     print("...")
#
# # Show the number of aliens that was created
# print("Total number of aliens: "+str(len(aliens)))


# A list in a dictionary

# Store information about a pizza being ordered
# pizza = {
#     'crust':'thick',
#     'toppings': ['mushrooms','extra cheese'],
#     }
#
# # summerize the order
# print(" you ordered a " + pizza['crust'] +" crust pizza with the followin toppings: ")
#
# for topping in pizza['toppings']:
#     print("\t" + topping)


# USers have more than one favorite language now

# fav_languages = {
#      'jen': ['python', 'ruby'],
#      'sarah': ['c'],
#      'edward': ['ruby', 'go'],
#      'phil': ['python', 'haskell'],
#      }
#
# for name,languages in fav_languages.items():
#     print("\n" + name.title() + "'s favorite languages are: ")
#     for language in languages:
#         print("\t" + language.title())




# A dictionary in a dictionary

# users = {
#     'aeinstein':{
#     'first_name':'albert',
#     'last_name':'einstein',
#     'location':'princeton',
#     },
#     'mcurie': {
#
#     'first_name': 'marie',
#     'last_name': 'curie',
#     'location': 'paris',
#     },
# }
#
# for username,user_info in users.items():
#     print("\nUsername: "+username.title())
#     user_full_name = user_info['first_name'] + " " + user_info['last_name']
#     user_location = user_info['location']
#
#     print("\t Full name: " + user_full_name.title())
#     print("\t Location: "+ user_location.title())


# 6.7 (People)

# people = []
#
# my_favorite_person = {
#     'first_name':'Fariha',
#     'last_name':'Zaman',
#     'age':18,
#     'city':'Warren',
#     'state':'Michigan.'
#     }
# people.append(my_favorite_person)
# my_favorite_person = {
#     'first_name':'Amina',
#     'last_name':'Bushar',
#     'age':21,
#     'city':'Paterson',
#     'state':'New Jersey.'
#     }
# people.append(my_favorite_person)
# my_favorite_person = {
#     'first_name':'Rahima',
#     'last_name':'Mahmood',
#     'age':65,
#     'city':'Paterson',
#     'state':'New Jersey.'
# }
# people.append(my_favorite_person)
#
#
#
# for person in people:
#     name = person['first_name'].title() + " " + person['last_name'].title()+ "."
#     age = str(person['age'])
#     location = person['city'].title() + "," + person['state'].title()
#     print("My favorite person is " + name + " She is " + age + " years old, and she lives in " + location)



# 6.8 (Pets)

pets = []

my_dog = {
    'animal type':'Dog',
    'animal name':'Neilan',
    'owners name':'I',
    'weight': 30,
    }
pets.append(my_dog)

bushras_cat = {
    'animal type':'a cute cat',
    'animal name':'box',
    'owners name':'Amina Bushra',
    'weight':15,
    }
pets.append(bushras_cat)
moms_bird = {
    'animal type':'Pigeon',
    'animal name':'flu',
    'owners name':'Rahima Mahmood',
    'weight': 5,
    }
pets.append(moms_bird)

for pet in pets:
    kind_of_animal = pet['animal type']
    animal_name = pet['animal name']
    animal_owner = pet['owners name']
    print(animal_owner.title() + " own a " + kind_of_animal.title()+ " and the name of the " + kind_of_animal.title() + " is "+  animal_name.title() + ".")
