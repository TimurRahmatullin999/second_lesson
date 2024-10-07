class Toy:

    def __init__(self, name, color, type):
        self.name = name
        self.color = color
        self.type = type

    def __str__(self):
        return f"Игрушка: {self.name}, цвет: {self.color}, тип: {self.type}"


class Factory:

    def making_toy(self, name, color, type):

        print(f"Подготовка закупки материала")

        self.purchase_of_raw_materials(name)

        print(f"Начинается пошивка")

        self.sewing(name)

        print(f"Несется краска")

        self.coloring(name, color)

        return Toy(name, color, type)

    def purchase_of_raw_materials(self, name):
        print(f"Материал для {name} куплен")

    def sewing(self, name):
        print(f"Пошивка для {name} выполена")

    def coloring(self, name, color):
        print(f"Игрушка {name} покрашена в {color} цвет")



Factory = Factory()

Rabbit = Factory.making_toy('Кролик', 'Белый', 'Lego')
print(Rabbit)
