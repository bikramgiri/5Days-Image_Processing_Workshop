class Sushma: # Class
    location = "Itahari"  # Attribute

    def __init__(self, id):  # Constructor
        self.id = id  # Attribute

    def slogan(self): # Method
        return "Best IT College" # Method output

# Creating an instance of Sushma class
godavari = Sushma(2)

# Printing attributes and method output
print(godavari.location)  # Accessing class attribute
print(godavari.slogan())  # Calling the method
print(godavari.id)  # Accessing instance attribute

# Output:
# Itahari
# Best IT College
# 2
