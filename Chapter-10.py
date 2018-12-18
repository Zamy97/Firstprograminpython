## reading from a file

# with open('text_files/pi_digits.txt')as file_object:
#     contents = file_object.read()
#     print(contents.strip())

## Read a file from a specific location

# with open('Specific file route')

## Absoulate path

# Absolute paths are usually longer than relative paths, so it’s helpful to store them in a variable and then pass that variable to open(). On Linux and OS X, absolute paths look like this:
# file_path = '/home/ehmatthes/other_files/text_files/filename.txt' with open(file_path) as file_object:

# Reading line by line from a file

''' filename = 'text_files/pi_digits.txt'

 with open(filename) as file_object:
     for line in file_object:
        print(line.strip())
'''

# Making a list of lines from a file

# filename = 'text_files/pi_digits.txt'
#
# with open(filename) as file_object:
#     lines = file_object.readlines()

# for line in lines:
#     print(line.strip())

# pi_string = ''
# for line  in lines:
#     pi_string += line.strip()
#
# birthday = input("Enter your birthday, in the form mmddyy: ")
# if birthday in pi_string:
#     print("Your birthday appears in the few digits of pi that I have collected!")
# else:
#     print("Your birthday does not appear in the first million digits of pi.")
#
# print(pi_string[:])
# print(len(pi_string))


# 10.1 (Learning Python)

# with open('summary.text') as file_name:
#     summary = file_name.read()
#     print(summary)
#     print(summary)
#     print(summary)

# with open('summary.text') as file_name:
#     lines = file_name.readlines()

# for line in lines:
#     print(line)

# pi_string = ''
# for line  in lines:
#     pi_string += line.strip()
# print(pi_string)
# pi_string.replace('Open', 'Fariha')
# print(pi_string)

#
# file_name = 'programming.text'
#
# with open(file_name, 'w') as file_object:
#     file_object.write("Goal is to work at Google.\n")
#     file_object.write("I am going to make is happen Inshallah.\n")
#
#
# with open(file_name, 'a') as file_object:
#     file_object.write("Because I can solve problems when I work at Google.\n")
#     file_object.write("And also make some good money uk wt m sayinn.\n")

## 10.3 (Guest)

# user_name = input("What is your name bro??")
#
# with open('names.txt','a') as file_object:
#     file_object.write(user_name + "\n")

## 10.4 (Guest Book)

# filename = 'names.txt'
#
# print("Enter 'quit' when you are finished.")
# while True:
#     name = input("\nWhat's your name? ")
#     if name == 'quit':
#         break
#     else:
#         with open(filename, 'a') as f:
#             f.write(name + "\n")
#         print("Hi " + name + ", you've been added to the guest book.")

## 10.5 (Programming Poll)

# filename = 'programming_poll.txt'
#
# responses = []
# while True:
#     response = input("\nWhy do you like programming? ")
#     responses.append(response)
#
#     continue_poll = input("Would you like to let someone else respond? (y/n) ")
#     if continue_poll != 'y':
#         break
#
# with open(filename, 'a') as f:
#     for response in responses:
#         f.write(response + "\n")

## try Catch Block
## Handling ZeroDivisionError error

# try:
#     print(6/0)
# except ZeroDivisionError:
#     print("You can't divide a number by 0")

## Simple Calculator

# print("Give me two numbers")
# print("Enter q to quit")
#
# while True:
#     first_number = input("\nFirst Number: ")
#     if first_number == 'q':
#         break
#     second_number = input("\nSecond Number: ")
#     if second_number == 'q':
#         break
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("Cmo'n now you can't divide a number by 0")
#     else:
#         print(answer)

## 10.6 (Addition) and 10.7
# print("Let's do some basic math")
# while True:
#     first_number = input("\nWhat is the first number that you want: ")
#     if first_number == 'q':
#         break
#
#     second_number = input("What is the second number that you want: ")
#     if second_number == 'q':
#         break
#
#     try:
#         addition_result = int(first_number) / int(second_number)
#     except ValueError:
#         print("Please type in a number")
#     else:
#         print(addition_result)

    ## 10.8 (Cats and Dogs)

filename = 'cats_and_dogs_name.txt'

with open(filename, 'w') as file_object:

    file_object.write("\n Mini")
    file_object.write("\n Spot")
    file_object.write("\n Sniper")
try:
    with open(filename) as file_object:
        stuff = file_object.read()
        print(stuff)
except FileNotFoundError:
    print("Please make sure the file exist first")
