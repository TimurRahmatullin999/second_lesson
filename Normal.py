class Person:

    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def attack(self, enemy):
        if self.__class__ == enemy.__class__:
            raise TypeError('Нельзя аттаковать своего союзника')
        print(f"{self.name} атакует {enemy.name}")
        enemy.count_health(self.damage)

    def count_health(self, damage):
        dam = self.__count_damage(damage)
        self.health -= dam
        self.health = max(0, self.health)
        return f"{self.name} получил(-а) {dam} ед.урона. Осталось {self.health} ед.жизни"

    def __count_damage(self, dam):
        taken_damage = dam - self.armor
        if taken_damage < 0:
            taken_damage = 0
        return taken_damage


class Enemy(Person):
    pass


class Player(Person):
    pass


class Game:

    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def game(self):
        start_game = 'p'
        while self.player.health > 0 and self.enemy.health > 0:
            if start_game == 'p':
                self.player.attack(self.enemy)
                start_game = 'e'
            else:
                self.enemy.attack(self.player)
                start_game = 'p'

        if self.player.health == 0:
            print(f"{self.enemy.name} выиграл(-а)")
        elif self.enemy.health == 0:
            print(f"{self.player.name} выиграл(-а)")


player = Player('Рик', 50, 30, 10)
enemy = Enemy('Чак', 50, 30, 30)
Game(player, enemy).game()
