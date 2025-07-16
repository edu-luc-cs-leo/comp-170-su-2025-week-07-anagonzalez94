# Creating the constructor
class Vehicle:
    def __init__(self, name, mpg):
        self.name = name
        self.mpg = mpg
    def fuel_needed(self, distance):
        return distance / self.mpg
    def description(self):
        return f"{self.name} gets {self.mpg} miles per gallon."
# Now rewriting the individual subclasses using the constructor "Vehicle"
class Car(Vehicle):
    def __init__(self):
        super().__init__("Car", 30)

class Truck(Vehicle):
    def __init__(self):
        super().__init__("Truck", 15)

class Motorcycle(Vehicle):
    def __init__(self):
        super().__init__("Motorcycle", 50)

class Bus(Vehicle):
    def __init__(self):
        super().__init__("Bus", 8)
# Test
if __name__ == "__main__":
    # Call new instances of objects created above
    vehicles = [Car(),Truck(),Motorcycle(),Bus()]
    # Iterate through every instance
    for vehicle in vehicles:
        print(vehicle.description)
        print(f"Fuel needed to go 100 miles: {vehicle.fuel_needed(100):.2f} gallons.")
#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  IF THERE IS ANY CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓         PLEASE DO NOT MODIFY IF       ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 