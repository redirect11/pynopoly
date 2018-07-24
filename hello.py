from player import Player
from prop import Prop
from prop import Station
from board import Board
from round_manager import RoundManager

if __name__ == '__main__':
    player = Player("Daniele", 1000)
    player2 = Player("peppe", 1000)
    props = (Prop("Vicolo Corto", 60, 30, 50, 2, 0, none=5, complete=8, one=10, two=20, three=30, four=50, hotel=60),
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
             )

    players = [player, player2]
    print(player)
    print(player2)
    board = Board(players, props)
    round_manager = RoundManager(board)

    print("starting...")
    round_manager.start_game()





