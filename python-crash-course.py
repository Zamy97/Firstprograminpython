# print("\thello python interpreter!")
#
# simple_message = " The best way yo understand new programming concept is to try using them in your programs."
#
# print(simple_message)
#
# simple_message = "And you are going to try to apply as much as possible and practice as much as possible to get good at it."
#
# # The (.) after simple_message tells python to perform the title() method on the variable simple_message.
#
# print(simple_message.title())
#
# # The (.) after the simple_message tells pythong to perform the upper() method on the variable simple_message. What .upper() is doing is it's telling python to make all the values of simple_message uppercase.
#
# print(simple_message.upper())
#
# # What .lower() method is doing here is it's telling python to make everything lowercase in the variable simple_message by performing that action.
#
# print(simple_message.lower())
#
#
# # What this is doing is it's telling the lstrip and rstrip to act on the iphone varible. What it'll do is it'll get rid of the space from both sides of the value of the variable.
# iphone = '     macs are really really expensive      '
# Macs = iphone.rstrip().lstrip()
# print(Macs.strip())
#
#
#
# message = "one of pytho's strengths is it's diverse community."
# print(message.title())
#
# age = 21
#
# birthday_wish = "Happy " + str(age) + "st Birthday"
# print(birthday_wish)

# coop_people = ['Andrea','Andrew', 'Saeed', 'jose', 'Gelle', 'edgardo']
# coop_people[2] = 'Antonio'
# print(coop_people)
# coop_people.append('Saeed')
# print(coop_people)

# What this is doing is it's inserting a value inside the existing list already. It's telling python that it needs to add an inside inside the list of empty_list. But it's specificly adding it in one position, for ex it's putting it right before hydro flask element.
# empty_list = ['aktar','hydro-flask','iphone']
# empty_list.insert(1, 'Macbook-pro')
# print(empty_list)
# del empty_list[2]
# print(empty_list)

# To pop an  item from the list you can use the pop method which will get rid of the last item from your list. However, you can use that item later. What is happening on the next line of code is where it's popping the last motocycle item from the list but then it's storing that value in a new variable so you can use that popped value later on if you want to.

motorcycles = ['Honda', 'Suzuki', 'yamaha','iphone', 'macbooks', 'water']
popped_motorcycle = motorcycles.pop(0)
# print(motorcycles)
# print(popped_motorcycle)
# cycle = "if I ever buy a motocycle, i'll buy a " + popped_motorcycle + "."
# print(cycle)

motorcycles.remove('water')
print(motorcycles)
