from math import *

Andrea = "She loves singing."

print(Andrea.replace("singing", "Dancing"))

Andrea = "She loves eating"

print(Andrea.replace("eating", "listening to music"))

number = 56

print(str(number) + " is my favorite number")

my_number = -24
print(abs(my_number))
print(abs(pow(my_number, 5)))
print(max(5,6,3,7,1,9,19))
print(min(9,5,3,0,1,4,6))
print(round(7.87887))
print(floor(9.7623623))
print(ceil(2.087497))
print(sqrt(8642))


name = input("What is your name: ")
Age = input("What is your age: ")

print("Hello " + name + "! you are years old " + Age )


first_number = input("enter a number")
second_number = input("enter another number")

result = float(first_number) + float(second_number)

print(result)




first_Verb = input("Enter a Verb: ")
plural_noun = input("Enter a Plural Noun: ")
celebrity = input("Enter a Celebrity Name: ")
country = input("Enter a Country Name: ")
your_name = input("Enter your name: ")






print( your_name +  " is good at " + first_Verb )
print("She loves everything about " + plural_noun )
print("She kinda wants to go to " + country + " to meet " + celebrity)


## List

friends = ["Andrea", "Tamim", "Fariha", "My Mom"]

print(friends)

lucky_numbers = [4,5,6,7,8,1,2,3,45,6]
friends = ["Andrea", "Tamim", "Fariha","Fariha", "My Mom"]

friends.extend(lucky_numbers)

friends.append("Anisha")

## what the next line will do is it will add the name kelly in the first index space and push all the other names to it's right.

friends.insert(1, "kelly")
##friends.remove("My Mom")


print(friends.index("Fariha"))
print(friends.count("Fariha"))

friends.sort()
lucky_numbers.sort()
lucky_numbers.remove()

friends2 = friends.copy()

print(friends2)

# Tuples

coordinates = (4,5,7)
print(coordinates[1])

## Function

def say_hi(name, age):
    print("hello " + name + " You are " + str(age) + " years old")

say_hi("Anisha", 45)
say_hi("Fariha", 36)


is_male = True
is_tall = True


if is_male and is_tall:
    print("you are a tall male")

elif is_male and not(is_tall):
    print("You are a short male")

elif not(is_male) and is_tall:
    print("You are not a male but are tall")

else:

    print("You are not a male and not tall")


def max_num(num1, num2, num3):

    if num1 >= num2 and num1 >= num3:

        return num1
    elif num2 >= num1 and num2 >= num3:

        return num2
    else:
        return  num3

print(max_num(3,4,5))

## Disctionaries

monthConversion = {

    "Jan": "january",
    "Feb": "february",
    "Mar": "March",
    "Apr": "April",
    "Jun": "Jun",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September"


}

print(monthConversion["Sep"])

##While loop

i = 20

while i <= 100:

    print(i)

    i += 2

print("Done with while loop")


##Game


secret_word = "Horse"

guess = ""
guess_count = 0
guess_limit = 5
out_of_guesses = False

while guess != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:

    print("out of guesses! You lost the game")
else:
    print("You win!")

## For Loop

bondhu = ["Jim", "Karen", "Akash", "Kevin"]


for friend in bondhu:
    print(friend)

for index in range(10):
    print(index)

for nmbr in range(4, 15):
    print(nmbr)

for bndu in range(len(bondhu)):
    print(bondhu[bndu])



def translate(phrase):
    translation = ""

    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))






































































