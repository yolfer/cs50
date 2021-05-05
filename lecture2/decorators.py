# just like you can modify a variable's value,
# decorators take a function and modify its behavior.
# takes a function as input, and returns a modified function

def announce(f):
    def wrapper():
        print("About the run the function...")
        f()
        print("Done with the function.")
    return wrapper

@announce
def hello():
    print("Hello, world!")

hello()