from engine.player import Player
from engine.prop import Prop
from engine.prop import Station
from engine.board import Board


class GameController:

    MAX_MONEY = 1000

    def __init__(self) -> None:
        super().__init__()
        # self.player = Player("Daniele", 1000)
        # self.player2 = Player("peppe", 1000)
        self.props = (Prop("Vicolo Corto", 60, 30, 50, 2, 0, none=5, complete=8, one=10, two=20, three=30, four=50, hotel=60),
                 Prop("Vicolo Stretto", 60, 30, 50, 2, 0, none=5, complete=8, one=10, two=20, three=30, four=50, hotel=60),
                 Station("Stazione Sud", 60, 200),
                 Prop("Bastioni Gran Sasso", 60, 30, 50, 3, 1, none=5, complete=8, one=10, two=20, three=30, four=50, hotel=60),
                 Prop("Viale Vesuvio", 60, 30, 50, 3, 1, none=5, complete=8, one=10, two=20, three=30, four=50, hotel=60),
                 Prop("Viale monte rosa", 60, 30, 50, 3, 1, none=5, complete=8, one=10, two=20, three=30, four=50, hotel=60),
                 Prop("Via Accademia", 60, 30, 50, 3, 2, none=5, complete=8, one=10, two=20, three=30, four=50, hotel=60),
                 Prop("Corso Ateneo", 60, 30, 50, 3,  2,  none=5, complete=8, one=10, two=20, three=30, four=50, hotel=60),
                 Prop("Piazza Università", 60, 30, 50, 3, 2, none=5, complete=8, one=10, two=20, three=30, four=50, hotel=60),
                 Prop("Via Verdi", 60, 30, 50, 3, 3, none=5, complete=8, one=10, two=20, three=30, four=50, hotel=60),
                 Prop("Corso Raffaello", 60, 30, 50, 3, 3, none=5, complete=8, one=10, two=20, three=30, four=50, hotel=60),
                 Prop("Piazza Dante", 60, 30, 50, 3, 3, none=5, complete=8, one=10, two=20, three=30, four=50, hotel=60),
                 Prop("Via Marco Polo", 60, 30, 50, 3, 4,  none=5, complete=8, one=10, two=20, three=30, four=50, hotel=60),
                 Prop("Corso Magellano", 60, 30, 50, 3, 4, none=5, complete=8, one=10, two=20, three=30, four=50, hotel=60),
                 Prop("Largo Colombo", 60, 30, 50, 3, 4, none=5, complete=8, one=10, two=20, three=30, four=50, hotel=60),
                 Prop("Largo Colombo", 60, 30, 50, 3, 4, none=5, complete=8, one=10, two=20, three=30, four=50, hotel=60),
                 Prop("Largo Colombo", 60, 30, 50, 3, 4, none=5, complete=8, one=10, two=20, three=30, four=50, hotel=60),
                 Prop("Largo Colombo", 60, 30, 50, 3, 4, none=5, complete=8, one=10, two=20, three=30, four=50, hotel=60),
                 Prop("Largo Colombo", 60, 30, 50, 3, 4, none=5, complete=8, one=10, two=20, three=30, four=50, hotel=60),
                 Prop("Largo Colombo", 60, 30, 50, 3, 4, none=5, complete=8, one=10, two=20, three=30, four=50, hotel=60),
                 Prop("Largo Colombo", 60, 30, 50, 3, 4, none=5, complete=8, one=10, two=20, three=30, four=50, hotel=60),
                 Prop("Largo Colombo", 60, 30, 50, 3, 4, none=5, complete=8, one=10, two=20, three=30, four=50, hotel=60),
                 Prop("Largo Colombo", 60, 30, 50, 3, 4, none=5, complete=8, one=10, two=20, three=30, four=50, hotel=60),
                 Prop("Largo Colombo", 60, 30, 50, 3, 4, none=5, complete=8, one=10, two=20, three=30, four=50, hotel=60),
                 Prop("Largo Colombo", 60, 30, 50, 3, 4, none=5, complete=8, one=10, two=20, three=30, four=50, hotel=60),
                 Prop("Largo Colombo", 60, 30, 50, 3, 4, none=5, complete=8, one=10, two=20, three=30, four=50, hotel=60),
                 Prop("Largo Colombo", 60, 30, 50, 3, 4, none=5, complete=8, one=10, two=20, three=30, four=50, hotel=60),
                 Prop("Largo Colombo", 60, 30, 50, 3, 4, none=5, complete=8, one=10, two=20, three=30, four=50, hotel=60),
                 Prop("Largo Colombo", 60, 30, 50, 3, 4, none=5, complete=8, one=10, two=20, three=30, four=50, hotel=60),
                 Prop("Largo Colombo", 60, 30, 50, 3, 4, none=5, complete=8, one=10, two=20, three=30, four=50, hotel=60),
                 Prop("Largo Colombo", 60, 30, 50, 3, 4, none=5, complete=8, one=10, two=20, three=30, four=50, hotel=60),
                 Prop("Largo Colombo", 60, 30, 50, 3, 4, none=5, complete=8, one=10, two=20, three=30, four=50, hotel=60),
                 Prop("Largo Colombo", 60, 30, 50, 3, 4, none=5, complete=8, one=10, two=20, three=30, four=50, hotel=60),
                 Prop("Largo Colombo", 60, 30, 50, 3, 4, none=5, complete=8, one=10, two=20, three=30, four=50, hotel=60),
                 Prop("Largo Colombo", 60, 30, 50, 3, 4, none=5, complete=8, one=10, two=20, three=30, four=50, hotel=60),
                 Prop("Largo Colombo", 60, 30, 50, 3, 4, none=5, complete=8, one=10, two=20, three=30, four=50, hotel=60),
                 Prop("Largo Colombo", 60, 30, 50, 3, 4, none=5, complete=8, one=10, two=20, three=30, four=50, hotel=60),
                 Prop("Largo Colombo", 60, 30, 50, 3, 4, none=5, complete=8, one=10, two=20, three=30, four=50, hotel=60),
                 Prop("Largo Colombo", 60, 30, 50, 3, 4, none=5, complete=8, one=10, two=20, three=30, four=50, hotel=60),
                 Prop("Largo Colombo", 60, 30, 50, 3, 4, none=5, complete=8, one=10, two=20, three=30, four=50, hotel=60),
                 Prop("Largo Colombo", 60, 30, 50, 3, 4, none=5, complete=8, one=10, two=20, three=30, four=50, hotel=60),
                 Prop("Largo Colombo", 60, 30, 50, 3, 4, none=5, complete=8, one=10, two=20, three=30, four=50, hotel=60),
                 Prop("Largo Colombo", 60, 30, 50, 3, 4, none=5, complete=8, one=10, two=20, three=30, four=50, hotel=60),
                 Prop("Largo Colombo", 60, 30, 50, 3, 4, none=5, complete=8, one=10, two=20, three=30, four=50, hotel=60),
                 Prop("Largo Colombo", 60, 30, 50, 3, 4, none=5, complete=8, one=10, two=20, three=30, four=50, hotel=60),
                 Prop("Largo Colombo", 60, 30, 50, 3, 4, none=5, complete=8, one=10, two=20, three=30, four=50, hotel=60),
                 Prop("Largo Colombo", 60, 30, 50, 3, 4, none=5, complete=8, one=10, two=20, three=30, four=50, hotel=60),
                 Prop("Largo Colombo", 60, 30, 50, 3, 4, none=5, complete=8, one=10, two=20, three=30, four=50, hotel=60),
                 Prop("Largo Colombo", 60, 30, 50, 3, 4, none=5, complete=8, one=10, two=20, three=30, four=50, hotel=60),
                 Prop("Largo Colombo", 60, 30, 50, 3, 4, none=5, complete=8, one=10, two=20, three=30, four=50, hotel=60),
                 )

        # self.players = [self.player, self.player2]
        # print(self.player)
        # print(self.player2)
        self.board = Board(self.props)

    def initialize(self):
        pass

    def start_game(self):
        pass

    def add_player(self, name, color):
        p = Player(name, GameController.MAX_MONEY, color)
        self.board.add_player(p)

    

