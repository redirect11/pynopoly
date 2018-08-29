import pygame
from ui.game_object import GameObject
from ui.py_game_box import Box
from ui.py_game_player import PyGamePlayer


class PyGameBoard(GameObject):
    def __init__(self, image_file):
        super().__init__()
        #self.board = board
        self.image_file = image_file
        self.box_sprites = pygame.sprite.Group()
        self.player_sprites = pygame.sprite.Group()
        self.players = []
        self.current_player = None

        self.image = pygame.image.load(self.image_file)
        self.image = pygame.transform.scale(self.image, (580, 580)).convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = [0, 0]
        self.rect.center = (1024/2, 600/2)

        # self.bg = pygame.Surface((580, 580))
        # self.bg_rect = pygame.rect.Rect(self.rect)

        self.boxes = [Box(i) for i in range(40)]
        self.box_sprites.add(self.boxes)

        # self.players = [PyGamePlayer(self.board.players[i], self.boxes[0]) for i in range(len(self.board.players))]
        #
        # self.player_sprites.add(self.players[0])
        # self.current_player = self.players[0]

    def on_init(self, n_players):
        super().on_init()
        self.players = [PyGamePlayer(id, self.boxes[0]) for id in n_players.keys()]
        self.player_sprites.add(self.players)
        self.current_player = self.players[0]
        print(n_players)
        for box in self.boxes:
            box.on_init()

    def on_event(self, event):
        super().on_event(event)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            print("left")
            self.move_current_player(1)
        if keys[pygame.K_RIGHT]:
            print("right")
            self.move_current_player(-1)

    def on_loop(self):
        super().on_loop()

    def on_render(self, screen):
        super().on_render(screen)
        screen.blit(self.image, self.rect)
        screen.fill([255, 255, 255])
        self.player_sprites.clear(screen, self.image)
        screen.blit(self.image, self.rect)
        #self.screen.blit(self.bg, self.bg_rect)
        if self.current_player is not None:
            self.current_player.on_render(screen)
        #self.box_sprites.draw(self.screen)
        self.player_sprites.draw(screen)

    def on_cleanup(self):
        super().on_cleanup()

    def move_current_player(self, how_many):
        new_pos = self.current_player.current_box.pos + how_many
        if 0 <= new_pos < 40:
            print("moving to {0}".format(new_pos))
            self.current_player.set_current_box(self.boxes[new_pos])



