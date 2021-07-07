class Car:
    def __init__(self, mark, model, year, speed=0):
        self.__mark = mark
        self.__model = model
        self.__year = year
        self.__speed = speed
        self.__engine = False

    def turn_engine(self):
        self.__engine = True
    @property
    def speed(self):
        return self.__speed
    def stop(self):
        self.__speed = 0
        return self.__speed
    def brake(self):
        if self.__engine:
            if self.__speed >=10:
                self.__speed -=10
            else:
                self.__speed = 0
        else:
            print('Turn on engine')
        return self.__speed
    def accelerate(self):
        if self.__engine:
            self.__speed +=10
        else:
            print('Turn on engine')
        return self.__speed
    def get_speed(self):
        return f'{self.__speed}km/h'


    def transmission(self,speed = None):
        if speed==0:
            self.transmission = 'N'
            self.__speed = 0
        if speed==0:
            self.transmission = 0
        if 0<speed<=15:
            self.transmission = 1
        if 15<speed<=30:
            self.transmission = 2
        if 30<speed<=45:
            self.transmission = 3
        if 45<speed<=70:
            self.transmission = 4
        return self.transmission, self.__speed

car_1 = Car('bmw','525',2010)
car_1.turn_engine()
car_1.accelerate()
car_1.accelerate()
car_1.accelerate()
b = car_1.accelerate()
print(car_1.get_speed())
print(car_1.transmission(b))


