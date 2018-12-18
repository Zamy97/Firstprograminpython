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

print(pi_string[:9])
print(len(pi_string))
