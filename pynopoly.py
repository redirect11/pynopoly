import os
import pygame

from pygame.compat import geterror
from pygame.locals import *

from board import Board
from player import Player
from prop import Prop
from prop import Station
import operator

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, 'data')


def load_image(name, colorkey=None):
    fullname = os.path.join(data_dir, name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        print('Cannot load image:', fullname)
        raise SystemExit(str(geterror()))
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()


def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer or not pygame.mixer.get_init():
        return NoneSound()
    fullname = os.path.join(data_dir, name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error:
        print ('Cannot load sound: %s' % fullname)
        raise SystemExit(str(geterror()))
    return sound


class PyNopoly:
    def __init__(self, players, props):
        self.players = players
        self.time = 0
        self.max = max
        self.rt = None
        self.game_started = False
        self.clock = pygame.time.Clock()

        # init pygame
        pygame.init()
        self.screen = pygame.display.set_mode((468, 60))
        pygame.display.set_caption('Pynopoly')
        pygame.mouse.set_visible(1)

        # Create The Background
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((250, 250, 250))
        # Put Text On The Background, Centered
        if pygame.font:
            font = pygame.font.Font(None, 36)
            text = font.render("Pummel The Chimp, And Win $$$", 1, (10, 10, 10))
            textpos = text.get_rect(centerx=self.background.get_width() / 2)
            self.background.blit(text, textpos)

        # Display The Background
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()
        board_img, board_rect = load_image('monopoly-hasbro.jpg', -1)
        self.board = Board(players, props, board_img, board_rect)
        self.allsprites = pygame.sprite.RenderPlain((self.board))

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
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.game_started = False
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    self.game_started = False
                # elif event.type == MOUSEBUTTONDOWN:
                #     if fist.punch(chimp):
                #         punch_sound.play()  # punch
                #         chimp.punched()
                #     else:
                #         whiff_sound.play()  # miss
                elif event.type == MOUSEBUTTONUP:
                    self.start_round(self.board.roll_dice)
                    if index == len(self.players)-1:
                        index = 0
                    else:
                        index = index + 1
                    self.board.set_current_player(self.players[index])
                    self.clock.tick(60)

            self.allsprites.update()

            # Draw Everything
            self.screen.blit(self.background, (0, 0))
            self.allsprites.draw(self.screen)
            pygame.display.flip()

        pygame.quit()

    def start_round(self, dice_result):
        self.board.move_player(dice_result())


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
    round_manager = PyNopoly(players, props)


    print("starting...")
    round_manager.start_game()








