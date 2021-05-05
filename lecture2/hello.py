print("Hello, world!")

# Some variable types
a = 28 # int
b = 1.5 # float
c = "Hello!" # str
d = True # bool
e = None # NoneType

name = input("Name: ")
print("Hello, " + name) # old way
print(f"Hello, {name}") # formatted strings

# Conditions
n = int(input("Number: "))

if n > 0:
    print("n is positive")
elif n < 0:
    print("n is negative")
else:
    print ("n is zero")
