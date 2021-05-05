class Point():
    def __init__(self, x, y): # automatically called for each new instance of Point
        # self represents the object instance itself
        self.x = x
        self.y = y

p = Point(2, 8) # don't provide `self`
print(p.x)
print(p.y)

# more complicated example
class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)
people = ["Harry", "Ron", "Hermione", "Ginny"]
for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No seats left for {person}!")
