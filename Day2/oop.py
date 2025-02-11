class Person:
    type  = "living"
    def __init__(self, name, age): # __init__  is Class constructor
        self.name = name
        self.age = age
  
    def speak(self):
        return ("Hello my name is " + self.name + ". My age is "+ str(self.age)+ ". I am a " + self.type + " being.")

p1 = Person("John", 36)

print(p1.type)
print(p1.name)
print(p1.age)
print(p1.speak())
