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
