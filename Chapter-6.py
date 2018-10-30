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


favorite_languages = {
       'jen': 'python',
       'sarah': 'c',
       'edward': 'ruby',
       'phil': 'python',
       }
friends = ['phil','sarah']
for name in sorted(favorite_languages.keys()):
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() + ", I see you love " +favorite_languages[name].title()+ "!")

if 'Erin' not in favorite_languages.keys():
    print(" HI Erin, please take our survey")


# Looping Through All Values in a Dictionary
