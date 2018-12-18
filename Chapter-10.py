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

filename = 'text_files/pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

# for line in lines:
#     print(line.strip())

pi_string = ''
for line  in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the few digits of pi that I have collected!")
else:
    print("Your birthday does not appear in the first million digits of pi.")

print(pi_string[:])
print(len(pi_string))


# 10.1 (Learning Python)

# with open('summary.text') as file_name:
#     summary = file_name.read()
#     print(summary)
#     print(summary)
#     print(summary)

with open('summary.text') as file_name:
    lines = file_name.readlines()

# for line in lines:
#     print(line)

pi_string = ''
for line  in lines:
    pi_string += line.strip()
print(pi_string)
pi_string.replace('Open', 'Fariha')
print(pi_string)
