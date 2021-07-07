class Dog:
    def __init__(self, name, weight, age,owner):
        self.__name = name
        self.__weight = weight
        self.__age = age
        self.__owner = owner
    def get_owner(self):
        print(self.__owner)
    def set_owner(self):
        return self.__owner
dog_1=Dog('asd',25,5,'dima')
dog_1.get_owner()
print(dog_1.set_owner())