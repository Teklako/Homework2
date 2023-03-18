#დავალება1
class Rectangle:
    def __init__(self, width, length, color):
        self.sigane = width
        self.sigrdze = length
        self.peri = color
    def area(self):
        return self.sigrdze * self.sigane
    def perimeter(self):
        return 2 * (self.sigane + self.sigrdze)
obj_1 = Rectangle(5, 1, "blue")
obj_2 = Rectangle(3, 3, "green")
obj_3 = Rectangle(7, 3,"purple")
print(obj_1.area())
#დავალება2
class Car:
    def __init__(self, color, brend, model):
        self.color = color
        self.brend = brend
        self.model = model
    def __str__(self):
        return f"მანქანის ფერი არის: {self.color}, ბრენდი არის: {self.brend}, მოდელი არის: {self.model}"
car_1 = Car( "orange",  "Ford",  "Mustang" )
print(car_1)
car_2 = Car( "Blue",  "Toyota", "Prius")
print(car_2)
car_3 = Car( "Green",  "Volkswagen", "Golf")
print(car_3)
#დავალება3
class Dog:
    def __init__(self, breed="Neaporitan Mastiff", size="Large", age="5 years" , color="Black" ):
        self.breed = breed
        self.size = size
        self.age = age
        self.color = color
    def __str__(self):
        return f"ჯიში არის: {self.breed}, ზომა არის: {self.size},ასაკი არის: {self.age}, ფერი არის: {self.color}"
    def sleep(self):
        return f"ძაღლს სძინავს 2 საათი"
    def Eat(self):
        return f",ძარლი ჭამს პურს,"
    def Sit(self):
        return "ძაღლი ზის კოხტად,"
    def Run(self):
        return "ძაღლი დარბის ძალიან სწრაფად."
dog_1 = Dog()
print(dog_1, dog_1.sleep(),dog_1.Eat(),dog_1.Sit(),dog_1.Run())
dog_2 = Dog("Maltese", "Small", "2 years", "White.")
print(dog_2, dog_2.sleep(), dog_2.Eat(), dog_2.Sit(), dog_2.Run())
dog_3 = Dog("Chow Chow", "Midium", "3 years", "Brown.")
print(dog_3,dog_3.sleep(), dog_3.Eat(), dog_3.Sit(), dog_3.Run())




