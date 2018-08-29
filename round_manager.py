import operator


class RoundManager:
    def __init__(self, board):
        self.players = board.players
        self.board = board
        self.rt = None
        self.game_started = False

    def __first_roll(self):
        results = []
        for player in self.players:
            results.append(player.roll_dice())
        index, value = max(enumerate(results), key=operator.itemgetter(1))
        return self.players[index], index

    def start_game(self):
        player, index = self.__first_roll()
        print("Complimenti '{0}' giocherai per primo".format(player.name))
        self.board.set_current_player(player)
        self.game_started = True

    def loop(self):
        input('Premi invio per lanciare i dadi')
        self.start_round(self.board.roll_dice)
        input("Premi invio per terminare il turno")
        # if index == len(self.players) - 1:
        #     index = 0
        # else:
        #     index = index + 1
        # self.board.set_current_player(self.players[index])

    def start_round(self, dice_result):
        self.board.move_player(dice_result())





