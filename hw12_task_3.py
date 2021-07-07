class Dog:
    def __init__(self, name, weight, age):
        self.__name = name
        self.__weight = weight
        self.__age = age
    def bark(self):
        print('woof')
    def jump(self):
        print('jump')
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, new_name):
        self.__name = new_name
    @property
    def weight(self):
        return self.__weight
    @weight.setter
    def weight(self, new_weight):
        self.__weight = new_weight
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, new_age):
        self.__age = new_age

dog_1 = Dog('rex', 25, 5)
print(dog_1.name)
dog_1.name = 'bob'
print(dog_1.name)

class Car:
    def __init__(self, mark, model, color):
        self.__mark = mark
        self.__model = model
        self.__color = color
    __speed = 0
    def accelerate(self):
        self.__speed +=30
        return self.__speed
    def brake(self):
        self.__speed -=30
        return self.__speed
    @property
    def mark(self):
        return self.__mark
    @mark.setter
    def mark(self, new_mark):
        self.__mark = new_mark
    @property
    def model(self):
        return self.__model
    @model.setter
    def model(self, new_model):
        self.__model = new_model
    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, new_color):
        self.__color = new_color
print('________________________________')
car_1 = Car('bmv','525','black')
print(car_1.color)
car_1.color = 'red'
print(car_1.color)
print(car_1.accelerate())
print('________________________________')
class Sofa:
    def __init__(self, width, height, color):
        self.__width = width
        self.__height = height
        self.__color = color
    def weight(self,weight):
        self.weight = weight
    def material(self):
        print('leather')
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, new_width):
        self.__width = new_width
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, new_height):
        self.__height = new_height
    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, new_color):
        self.__color = new_color
sofa_1 = Sofa(190,90,'grey')
sofa_1.material()
print(sofa_1.height)
sofa_1.color = 'green'
print(sofa_1.color)