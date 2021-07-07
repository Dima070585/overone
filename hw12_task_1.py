class Car:
    def __init__(self, mark, model, year):
        self.mark = mark
        self.model = model
        self.year = year

    __speed = 0

    def accelerate(self):
        self.__speed +=20
        #return self.speed
    def brake(self):
        self.__speed = 0
        #return self.speed
    def chek_speed(self):
        return self.speed
car_1 = Car('bmw','5', '2015')
print(car_1.mark)
print(car_1.model)
print(car_1.year)

print(car_1.accelerate())
print(car_1.brake())
