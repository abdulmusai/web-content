# Define a class
class Car:
    # Constructor: Initializes the attributes
    def __init__(self, brand, model, year):
        self.brand = brand  # Attribute
        self.model = model
        self.year = year
    # Method to display car details
    def display_info(self):
        print(f"{self.brand} {self.model}, {self.year}")

# Create an object of the class
my_car = Car("Toyota", "Corolla", 2022)
# Access attributes and methods
print(my_car.brand)  # Output: Toyota
my_car.display_info()  # Output: Toyota Corolla, 2022
4 * 4

