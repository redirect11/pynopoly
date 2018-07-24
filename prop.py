class Prop:
    MAX_HOUSE = 4

    def __init__(self, name, price, lien, house_price, class_count, klass, **taxes):
        self.name = name
        self.price = price
        self.lien = lien
        self.house_price = house_price
        self.taxes = taxes
        self.owner = None
        self.n_house = 0
        self.klass = klass
        self.class_count = class_count

    def sell_to(self, player):
        if self.owner is None:
            self.owner = player
            player.give_money(self.price)
            return True
        print("returning false")
        return False

    def add_house(self, house_n):
        n_house = self.n_house + house_n
        enough_money = self.owner.get_money() - (house_n * self.house_price) < 0
        if n_house > Prop.MAX_HOUSE:
            print("troppe case. Puoi comprarne massimo '{0}'".format(Prop.MAX_HOUSE - self.n_house))
        elif not enough_money:
            print("Non hai abbastanza soldi per comprare tutte queste case")  # spostare questi print nella classe home
            # trovare un altro meccanismo per gestire l'aggiunta di una casa. Le stringhe sono presentazione e vanno
            # messe altrove
        else:
            self.n_house = n_house

    def get_tax(self, series_count):
        if series_count < self.class_count:
            return self.taxes['none']
        else:
            if self.n_house == 0:
                return self.taxes['complete']
            elif self.n_house == 1:
                return self.taxes['one']
            elif self.n_house == 2:
                return self.taxes['two']
            elif self.n_house == 3:
                return self.taxes['three']
            elif self.n_house == 4:
                return self.taxes['four']
            elif self.n_house == 5:
                return self.taxes['hotel']

    def __str__(self):
        return "name '{0}' price '{3}' taxes '{1}' owner '{2}'\n".format(self.name, self.taxes, self.owner, self.price)

    def __repr__(self):
        return self.__str__()


class Station(Prop):
    def __init__(self, name, lien, price=200):
        super().__init__(name, price, lien, house_price=0, class_count=4, klass=50, taxes=None)

    def get_tax(self, series_count):
        if series_count == 1:
            return 25
        if series_count == 2:
            return 50
        if series_count == 3:
            return 100
        if series_count == 5:
            return 200


class Company(Prop):
    def __init__(self, name, lien, price):
        super().__init__(name, price, lien, house_price=0, class_count=2, klass=80, taxes=None)

    def get_tax(self, series_count):
        if series_count == 1:
            return self.owner.roll_dice() * 4
        if series_count == 2:
            return self.owner.roll_dice() * 10
