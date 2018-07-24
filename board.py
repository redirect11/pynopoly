class Board:
    def __init__(self, players, props):
        self.players = players
        self.props = props
        self.__current_player = None

    def set_current_player(self, player):
        print("\nE' il tuo turno '{0}'".format(player.name))
        print(player)
        self.__current_player = player

    def roll_dice(self):
        if self.__current_player is not None:
            result = self.__current_player.roll_dice()
            print("'{1}' Hai totalizzato '{0}'".format(result, self.__current_player.name))
            return result

    def move_player(self, how_many):
        # self.__current_player = self.players[player_n]
        self.__current_player.calculate_current_pos(how_many)
        next_prop_index = self.__current_player.get_current_pos()-1
        if next_prop_index <= len(self.props):
            prop = self.props[next_prop_index]
        else:
            prop = self.props[next_prop_index - len(self.props)]
            print("Sei passato dal via. Guadagni 200")
            self.__current_player.get_money(200)
        print("Sei finito su: '{0}' ".format(prop.name))
        if prop.owner is None:
            print("La proprietà è libera")
            action = " "
            while action not in "SN":
                action = input("Vuoi comprare '{0}' ? [S/N]".format(prop.name)).upper()
                if action not in "SN" or len(action) != 1:
                    action = " "  # workaround. To find another way
                    print("Scrivi S oppure N")
            if action == 'S':
                # print("money: '{0}', prop.price: '{1}'".format(self.__current_player.money, prop.price))
                if self.__current_player.money >= prop.price:
                    if not prop.sell_to(self.__current_player):
                        print("La proprietà è già venduta")
                else:
                    print("Non hai abbastanza soldi")

        else:
            if self.__current_player.name == prop.owner.name :
                print("E' una tua proprietà")
            else:
                print("La proprietà è di '{0}'".format(prop.owner.name))
                payment_due = self.__calculate_due_payment(prop)
                print("Devi pagare '{0}'".format(payment_due))
                self.__current_player.pay_player(prop.owner, payment_due)

    def __calculate_due_payment(self, prop):
        series_count = len([i for i in self.props if i.owner is not None and prop.owner.name == i.owner.name
                            and i.klass == prop.klass])
        print("series count: '{0}'".format(series_count))
        return prop.get_tax(series_count)

