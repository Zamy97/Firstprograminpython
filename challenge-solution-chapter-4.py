# # Starting of chapter 4
#
# # HOw for loop stores info in the variable and print them out all of the ones from the list!
# magicians = ["Fariha", "David", "Carolina"]
# for magician in magicians:
#     print(magician.title() + ", that was a great trick!"  + "\n" +  "I can't wait to see the next trick" + "\n")
# ## Examples of good good naming in python
#  ## for cat in cats:
#  ## for dog in Dogs:
#  ## for item in list_of_items:
#
# print("Thank you for a great magic show")
#
# # 4.1 (Pizza)
#
# favorite_pizza = ["Mushroom pizza", "Slivers Pizza", "Veggie Pizza", "Any type of pizza"]
#
# message = "you know I love any type of pizza! It doesn't matter the kind to me"
#
# for pizza in favorite_pizza:
#     print(pizza + "\n" + "I love pizza, to me the kind doesn't matter at all" + "\n")
#
# print("Omg I can't explain to you how much I love " + favorite_pizza[1] + "\n" )
#
# # 4.2 (Animals)
#
# animal_list = ["Dog", "Cat","cow","Sagol"]
#
# for every_animal in animal_list:
#     print( "A "+ every_animal.title() + " would be a great pet for your fam." + "\n")
#
# print("These are some of the greatest animal that could be a great fit for your house")
#
# # Making a numerical list
#
# for value in range(1,10):
#     print(value)
#
# # Making a list using Range
#
# numbers = list(range(1,9))
# print(numbers)
#
# # Print umbers by even numbers
# even_numbers = list(range(2,23,2))
# print(even_numbers)
#
# ## Here's how you might put the first 10 square numbers into a list:
#
# squares = []
# for value in range(1,11):
#     square = value**2
#     squares.append(square)
#     # A cleaner way to write this would be this!
#     squares.append(value**2)
#
#
# print(squares)
#
# # using List comprehension compress the same lines of code in one line that you had to write three lines for!
#
# list_comprehension_list = [value**2 for value in range(1,50)]
# print(list_comprehension_list)
#
# # 4.3 (Counting to Twenty)
#
# one_thru_twenty = list(range(1,21))
# print(one_thru_twenty)
#
# # 4.4
#
# one_thru_million = list(range(1,1000000))
#
# for number in one_thru_million:
#     print(number)
#
# # 4.6
# one_thru_twenty_odd = list(range(1,21,2))
# print(one_thru_twenty_odd)
#
# # 4.8
#
# cubes_list = []
# for value in range(1,10):
#     cube = value**3
#     cubes_list.append(cube)
#
# print(cubes_list)
#
# # 4.9
#
# first_ten_numbers_cubes_list = [value**3 for value in range(1,11)]

# Slicing a list!

players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[3:4])

# If you don't give a starting value it'll start from the beginning of the list until the number you provide.
# If you don't provide any ending value it'll do the same thing! it'll start from the value you provided and it'll return every value after thiis.
# print(players[:4])
# print(players[1:])

# Looping thru a slice in tge list

# for player in players[:4]:
#     print(player.title())

# Copying a list




my_foods = ['pizza', 'falafel', 'carrot cake']
friends_food = my_foods[:]
print(friends_food)
