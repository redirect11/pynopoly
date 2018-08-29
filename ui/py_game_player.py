import pygame
import pygame.gfxdraw
from ui.game_object import GameObject
from ui.py_game_box import Box


class PyGamePlayer(GameObject):
    def __init__(self, id, start_box: Box):
        super(PyGamePlayer, self).__init__()
        self.position = [start_box.rect.x, start_box.rect.y]
        self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = start_box.rect.x + 15
        self.rect.y = start_box.rect.y + 15
        self.current_box = start_box
        self.id = id

        # draw.circle is not anti-aliased and looks rather ugly.
        # pygame.draw.circle(ATOM_IMG, (0, 255, 0), (15, 15), 15)
        # gfxdraw.aacircle looks a bit better.
        #pygame.gfxdraw.aacircle(self.image, 15, 15, 14, (0, 255, 0))
        #pygame.gfxdraw.filled_circle(self.image, 15, 15, 14, (0, 255, 0))

    # def update(self, *args):
    #     super().update(*args)
    #     if self.box_rect is not None:

    def set_current_box(self, box: Box):
        self.old_box = self.current_box
        self.current_box = box

    def on_init(self):
        super().on_init()

    def on_event(self, event):
        super().on_event(event)

    def on_loop(self):
        super().on_loop()

    def on_render(self, screen):
        super().on_render(screen)
        #self.image.fill([255, 255, 255])
        self.rect.x = self.current_box.rect.x + 5
        self.rect.y = self.current_box.rect.y + 5
        #print("x: {0} y: {0}".format(self.rect.x, self.rect.y))
        pygame.gfxdraw.aacircle(self.image, 15, 15, 10, (0, 255, 0))
        pygame.gfxdraw.filled_circle(self.image, 15, 15, 10, (0, 255, 0))
        #pygame.draw.circle(self.image, (0, 255, 0), (15, 15), 15)

    def on_cleanup(self):
        super().on_cleanup()

