# A Simple function
def greet_user(username):
    """Display a simple greeeting."""
    print("Hello "+ username.title()+ "!")

greet_user("Aktar")


# 8.1 (Message)
def display_message():
    print("I am learning about functions in this chapter because I am not comfortable with how to write them so I want to learn it in this chapter and be good at it! Uk wt m sayinn")

display_message()

# 8.2 (Favorite book)

def favorite_book(title):
    print("One of my favorite book is :" + title.title())

favorite_book(" If Beale Street could talk")



# POsitional function

def describe_pet(pet_name,animal_type = "Cat"):
    """Display information about a pet"""
    print("I have a "+animal_type.title()+".")
    print("My " + animal_type.title() + "'s name is " +pet_name + ".")

describe_pet("Goru")
describe_pet("leina",animal_type = "Horse",)
# A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')
# A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')


# 8.3(T-Shirts)

def make_shirts(shirt_size,message_on_shirt):
    print("You ordered a " + shirt_size.upper() + " size shirt. And the message it's going to have is: "+ message_on_shirt.title())

make_shirts("M","Sky is the limit.")
make_shirts(message_on_shirt = "If they can do it, I can do it too!",shirt_size = "M")
