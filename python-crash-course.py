print("\thello python interpreter!")

simple_message = " The best way yo understand new programming concept is to try using them in your programs."

print(simple_message)

simple_message = "And you are going to try to apply as much as possible and practice as much as possible to get good at it."

# The (.) after simple_message tells python to perform the title() method on the variable simple_message.

print(simple_message.title())

# The (.) after the simple_message tells pythong to perform the upper() method on the variable simple_message. What .upper() is doing is it's telling python to make all the values of simple_message uppercase.

print(simple_message.upper())

# What .lower() method is doing here is it's telling python to make everything lowercase in the variable simple_message by performing that action.

print(simple_message.lower())


# What this is doing is it's telling the lstrip and rstrip to act on the iphone varible. What it'll do is it'll get rid of the space from both sides of the value of the variable.
iphone = '     macs are really really expensive      '
Macs = iphone.rstrip().lstrip()
print(Macs.strip())



message = "one of pytho's strengths is it's diverse community."
print(message.title())

age = 21

birthday_wish = "Happy " + str(age) + "st Birthday"
print(birthday_wish)
