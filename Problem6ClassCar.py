# Emanuel Ramos
# 11/15/2022
#
# Description:

class Car:

    def __init__(self, model, year, color, type, manufacturer):
        self.model = model
        self.year = year
        self.color = color
        self.type = type
        self.get_manufacturer = manufacturer

    def get_model(self):
        return self.model()

    def get_year(self):
        return self.year()

    def get_color(self):
        return self.color()

    def get_type(self):
        return self.get_type()

    def get_manufacturer(self):
        return self.get_manufacturer()

    def fullspecs(self):
        return self.model + '' + str(self.year) + '' + self.color + '' + self.type + '' + self.get_manufacturer


car1 = Car("Sports", 2012, "Blue", "911", "Porsche")
car2 = Car("Sedan", 2020, "Black", "Jetta", "Volkswagen")

print(car1.get_color())
print(car1.get_model())
print(car1.get_type())
print(car1.get_manufacturer())
print(car1.fullspecs())
print(car2.get_color())
print(car2.get_model())
print(car2.get_type())
print(car2.get_manufacturer())
print(car2.fullspecs())
