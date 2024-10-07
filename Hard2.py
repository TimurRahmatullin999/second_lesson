class LegoToy:

    def __init__(self, name, color, type):
        self.name = name
        self.color = color
        self.type = type

    def __str__(self):
        return f"Лего-Игрушка: {self.name}, цвет: {self.color}, тип: {self.type}"



class CarToy(LegoToy):

    def __str__(self):
        return f"Машинка: {self.name}, цвет: {self.color}, тип: {self.type}"



class SoldierToy(LegoToy):
    pass


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
        else:
            return SoldierToy(name, color, type)

    def purchase_of_raw_materials(self, name):
        print(f"Материал для {name} куплен")

    def sewing(self, name):
        print(f"Пошивка для {name} выполена")

    def coloring(self, name, color):
        print(f"Игрушка {name} покрашена в {color} цвет")



Factory = Factory()

Rabbit = Factory.making_toy('Кролик', 'Белый', 'Lego')

print(Rabbit)