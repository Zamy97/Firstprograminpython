import random
import sys
import os

#Different types of data types in python.
#numbers, Strings, lists,Tuples, Dictionaries

#if you want to have a quote inside python you do it like the following:

quote = "\"Don't give up on learning coding"

#To join two strings together you can use '+' to do that. For ex:

adding_two_strings = '''you got this'''
new_string = "quote" + "adding_two_strings"

#A bit about lists
make_school_staff = ['Dan', 'Bruce', 'Megan', 'Dani']
print('My coach is', make_school_staff[0])

#To Change the value of the list you can do so as the following:

make_school_staff[1]="Jeremy"
print("Now the second person is", make_school_staff[1])

#To print a subset of the list you can do so by doing this:
print(make_school_staff[0:3]) #But remember the index 3 would not print here.Yes unfortunately that's how python isself.

#To combine two lists together you can do so by doing the following:
make_school_Students = ["Nathan","Asim", "Sarin", "Rinni", "Bri", "Anisha" ]

make_school = [make_school_staff, make_school_Students]
print(make_school)

#To get specific item from that list you do the following:
print(make_school[1][5])

#To add something at the end of your list you can do so by using the append function:
make_school_Students.append("Don")

#To add something at a specific location inside list you can do so by doing the following:
make_school_Students.insert(1, "pickle")

 #Few other data structing functions

 make_school_Students.sort()
 make_school_Students.remove()
 make_school_Students.reverse()

 #To delete something from a list you can do so by:

 del make_school_Students[3]

 #To get a length of the list you can do so by;
 print(len(make_school_Students))

# A bit about Tupoles {It's very similar to list}
# Once you create a tuple you can't change the valuve of it anymore.

aktar = (3,4,5,6,7)
new_aktar = list(aktar)
new_list = tuple(new_aktar)

#To get a list of your tuple you can get it by typing
len(tupple)
min(tuple)
max(tuple)

#A bit about Dictionary[you can join dictionaries with list with + sign ]

people_at_mke_scl = {'Dan': 'coach', 'Megan': 'student_service', 'Dani': 'BEW Teacher', 'bruce': 'my bew teacher'}

print(people_at_mke_scl['Dani'])

# To delete an entry inside a dictionary you can do so with the following.

del people_at_mke_scl['Megan']

# To change the value of an entry you can do the following.

people_at_mke_scl['Dan'] = 'Spd teacher'

# To see the number of stuff you have inside your dictionary. Do the following:

print(len(people_at_mke_scl))

#Get the value by passing a key from the Dictionary

print(people_at_mke_scl.get('Megan'))

#Get the keys from your dictionary

print(people_at_mke_scl.keys())

#Get the valyes from your dictionary

print(people_at_mke_scl.values())

# A bit about conditionals
#[if else elif --> are used to form different conditions based of different condition. == --> equal to, != --> not equal to, > --> greater than, >= --> greater than or equal to, < --> less than , or <= --> less than or equal to.
# If statement is going to excute if a condition is match.

age = 21

if age > 16 :
    print('You are old enough to drive')
else:
    print('you are not old enough to drive')

# bit about elif confdition

if age >= 21 :
    print('you can drive a truck')
elif age >= 16:
    print('you can drive a car')
else:
    print('you are not old enough to drive')

# Conbine condition with logical operator. They are [ and or not]

if ((age >= 10) and (age <= 18)):
    print('you are going to b done with high school')
elif (age == 19) or (age >= 50):
    print('you are going to be done with college ')
elif not(age==30):
    print('you failed with your life')
else:
    print("you don't get anything")

# A bit about looping
## For loop

for x in range(0, 10):
    print(x, '', end="")

# To create a new line you can do so by doing the following:

print('\n')

# Use for look to cycle thruough a list:

grocery_list = ['juice', 'Tomatoes', 'Mango', 'Banana', 'chips']

for y in grocery_list:
    print(y)

# To loop through a cycle using number do the follwoing:

for x in [2,4,6,8,10]:
    print(x)

num_list = [[1,2,3],[13,45,63,54], [500,700,500,498]]
for x in range(0,3):
    for y in range(0,3):
        print(num_list[x][y])

# A bit about while loop
# They are going to be use when you don't have any idea ahead of time how many times you are going to loop.



# This will generate a random number from 0-99
random_number = random.randomrange(0,100)

# What this is doing here is it has a condition to loop through until it hits 15. It's going to continure producing random number until It get's to 15 and as soon as it hits that it'll jump out of the loop.
while(random_number != 15):
    print(random_number)
    random_number = random.randomrange(0,100)

i = 0;

while( i <= 22):
    if(i%2 == 0):
        print(i)
    elif (i == 9):
        break
    else:
        i += 1 # i = i + 1
        continue

# A bit about functions:

def addNumber(fNum, lNum):
    sumNum = fNum + lNum
    return sumNum

string = addNumber(3,667)

# The varible that is created inside a function, you can't call that outside of the function. For ex: from the upper example you can't call 'sumNum' outside anywhere else. It means it's out of scope.

# A bit about Strings

# This will pring out the first 6 string from the variable.
 long_String = " I'll catch you if you fall"
 print(long_String[0:6])

 #Pring last 5 character
 print(long_String[-5:])

 #print everything up to the last 5 character
 print(long_String[:-5])

 # Join two strings together
 pring(long_String[:4] + "be there")

 # If you want to output a character using your input you can do so with the following.
 print("%c  is my %s letter and my number %d number is %.5f" % ()'x', 'favorite', 1, .14))

# Capitalize the first letter of a string
print(long_String.Capitalize())

# Find the index value of the start of a string
print(long_String.find("fall"))

#True or false of the character that have been entered in a string
print(long_String.isalpha())
print(long_String.isalnum())
print(len(long_String))
print(long_String.replace("fall", "ground"))
print(long_String.strip())
quote_list = long_String.split(" ")
print(quote_list)


# A bit about objects

class Animal:
    __name = None
    __height = 0
    __weight = 0
    __sound = 0

    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

    def set_name(self, name):
        self.__name = name

    def set_height(self, height):
        self.__height = height

    def set_weight(self, weight):
        self.__weight = weight

    def set_sound(self, sound):
        self.__sound = sound

    def get_name(self):
        return self.__name

    def get_height(self):
        return self.__height

    def get_weight(self):
        return self.__weight

    def get_sound(self):
        return self.__sound


    def get_type(self):
        print("Animal")

    def toSorting(self):
        return "{} is {} cm tall and {} kilogerms and say {}".format(self.__name, self.__height, self.__weight, self.__sound)

cat = Animal('Bella', 33,55, 'Meow')
print(cat)

# INheritence

class Dog(Animal):
    __owner = ""

    def __init__(self, name, height, weight, sound, owner):
        self.__owner = owner
        super(Dog, self).__init__(nsme,height,weight,sound)

    def set_owner(set, owner):
        self.__owner = __owner

    def get_owner(self):
        return self.__owner

    def get_type(self):
        print("Dog")

    def toSorting(self):
        return "{} is {} cm tall and {} kilogerms and says {} His owner is {}".format(self.__name, self.__height, self.__weight, self.__sound, self.__owner)


# A bit about Polymorphism
