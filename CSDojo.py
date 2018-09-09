# Function is collection of instruction that does something.

def function1():
    print("Hello Fariha")
    print("Hello Tasnima")

# To call a function you can just use the name of the function to call them. The next line would pring out the values inside it.
function1()

# A function could take parameters of argument. Whatever you have inside the parenthasis that is what known as parameter.
def function2(X):
    return 9*X
new_value = function2(8)
test_value1 = new_value * function2(10)
print(test_value1)


# Function could take more than one argument. For ex:

def function3(x,y):
    return x*y
function3_value = function3(8,6)
print(function3_value)
