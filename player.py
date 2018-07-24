from random import randint


class Player:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.current_pos = 0

    def pay_player(self, player, how_much):
        print("stai pagando '{0}'".format(how_much))
        self.give_money(how_much)
        player.get_money(how_much)

    def calculate_current_pos(self, how_many):
        self.current_pos = self.current_pos + how_many

    def get_current_pos(self):
        return self.current_pos

    def give_money(self, how_much):
        self.money = self.money - how_much

    def get_money(self, how_much):
        self.money = self.money + how_much

    @staticmethod
    def roll_dice():
        return randint(2, 12)

    def __str__(self):
        return "Nome: '{0}' - Soldi: '{1}'".format(self.name, self.money)

