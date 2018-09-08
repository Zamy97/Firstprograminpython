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
