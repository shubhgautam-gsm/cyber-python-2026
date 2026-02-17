class Car:
    def __init__(self, color ,name):
        self.color = color
        self.name = name
        
    def display_details(self):
        return self.color + " " + self.name


# car1={}
car1= Car('red','bmw')
car2= Car('green','mercedez')
car3= Car('orange','audi')

# car{
#     "color": "red",
#     "name": "bmw"
# }
print(car1.display_details())
print(car2.display_details())
print(car3.display_details())