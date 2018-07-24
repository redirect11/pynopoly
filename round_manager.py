from repeted_timer import RepeatedTimer
import operator


class RoundManager:
    def __init__(self, board):
        self.players = board.players
        self.board = board
        self.time = 0
        self.max = max
        self.rt = None
        self.game_started = False

    def __count(self, max, post_execute, args):
        self.time = self.time + 1
        if self.time == max:
            self.rt.stop()
            post_execute(args)
        else:
            print("%s!" % self.time)

    # not used for now
    def start(self, max, pre_execute, post_execute, pre_args, post_args):
        try:
            self.rt = RepeatedTimer(1, self.__count, max, post_execute,
                                    post_args)  # it auto-starts, no need of rt.start()
            # input("Premi invio tasto per lanciare i dati\n")
            pre_execute(pre_args)
        finally:
            print("FInally")
            self.time = 0
            self.rt.stop()

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
        while self.game_started:
            # self.start(10, input, self.start_round, "Premi Invio per lanciare i dadi\n", self.board.roll_dice)
            input('Premi invio per lanciare i dadi')
            self.start_round(self.board.roll_dice)
            input("Premi invio per terminare il turno")
            if index == len(self.players)-1:
                index = 0
            else:
                index = index + 1
            self.board.set_current_player(self.players[index])

    def start_round(self, dice_result):
        self.board.move_player(dice_result())





