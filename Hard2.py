class Toy:

    def __init__(self, name, color, type):
        self.name = name
        self.color = color
        self.type = type

    def __str__(self):
        return f"Игрушка: {self.name}, цвет: {self.color}, тип: {self.type}"


class LegoToy(Toy):
    def __str__(self):
        return f"Лего-Игрушка: {self.name}, цвет: {self.color}"



class CarToy(Toy):

    def __str__(self):
        return f"Машинка: {self.name}, цвет: {self.color}"



class SoldierToy(Toy):

    def __str__(self):
        return f"Солдатик: {self.name}, цвет: {self.color}"


class Factory:

    def making_toy(self, name, color, type):

        print(f"Подготовка закупки материала")

        self.purchase_of_raw_materials(name)

        print(f"Начинается пошивка")

        self.sewing(name)

        print(f"Несется краска")

        self.coloring(name, color)

        if type == 'Lego':
            return LegoToy(name, color, type)
        elif type == 'Car':
            return CarToy(name, color, type)
        elif type == 'Soldjer':
            return SoldierToy(name, color, type)
        else:
            raise TypeError('Такие типы игрушек не изготовляются')

    def purchase_of_raw_materials(self, name):
        print(f"Материал для {name} куплен")

    def sewing(self, name):
        print(f"Пошивка для {name} выполена")

    def coloring(self, name, color):
        print(f"Игрушка {name} покрашена в {color} цвет")



Factory = Factory()

Rabbit = Factory.making_toy('Кролик', 'Белый', 'Lego')
car = Factory.making_toy('Lambo Urus', 'BLUE', 'Car')
sold = Factory.making_toy('Скала', 'Бежевый', 'Soldjer')
print(Rabbit)
print(car)
print(sold)
