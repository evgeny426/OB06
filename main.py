# Задание: Разработать консольную игру "Битва героев" на Python с использованием классов и разработать план проекта по
# этапам/или создать kanban доску для работы над данным проектом
# Общее описание:
# Создайте простую текстовую боевую игру, где игрок и компьютер управляют героями с различными характеристиками. Игра состоит из раундов,
# в каждом раунде игроки по очереди наносят урон друг другу, пока у одного из героев не закончится здоровье.
#
# Требования:
# Используйте ООП (Объектно-Ориентированное Программирование) для создания классов героев.
# Игра должна быть реализована как консольное приложение.
# Классы:
# Класс Hero:
# Атрибуты:
# Имя (name)
# Здоровье (health), начальное значение 100
# Сила удара (attack_power), начальное значение 20
# Методы:
# attack(other): атакует другого героя (other), отнимая здоровье в размере своей силы удара
# is_alive(): возвращает True, если здоровье героя больше 0, иначе False
# Класс Game:
# Атрибуты:
# Игрок (player), экземпляр класса Hero
# Компьютер (computer), экземпляр класса Hero
# Методы:
# start(): начинает игру, чередует ходы игрока и компьютера, пока один из героев не умрет. Выводит информацию о каждом ходе (кто атаковал и сколько
# здоровья осталось у противника) и объявляет победителя.

import random


class Hero:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -= self.attack_power

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def start(self):
        turn = random.choice([self.player, self.computer])

        while self.player.is_alive() and self.computer.is_alive():
            if turn == self.player:
                turn.attack(self.computer)
                print(
                    f"{turn.name} attacks {self.computer.name}! {self.computer.name} has {self.computer.health} health left.")
                turn = self.computer
            else:
                turn.attack(self.player)
                print(
                    f"{turn.name} attacks {self.player.name}! {self.player.name} has {self.player.health} health left.")
                turn = self.player

        if self.player.is_alive():
            print(f"{self.player.name} wins!")
        else:
            print(f"{self.computer.name} wins!")


warrior = Hero("Warrior", 100, random.randint(20, 30))
monster = Hero("Monster", 100, random.randint(20, 30))
game = Game(warrior, monster)
game.start()