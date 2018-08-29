from ui.game_object import GameObject
from ui.py_game_prop import PyGameProp
import pygame

class Box(GameObject):

    WIDTH = 45.8
    HEIGHT = 75

    def __init__(self, pos) -> None:
        super().__init__()
        self.pos = pos

        if pos % 10 != 0:
            if 0 < pos < 10:
                print("pos 0:10: {0}".format(pos))
                self.image = pygame.Surface([Box.WIDTH, Box.HEIGHT])
                self.image.fill((255, 255, 255))
                self.image.set_colorkey((255, 255, 255))
                self.rect = self.image.get_rect()
                self.rect.x = 481 - ((Box.WIDTH - 1) * pos)
                self.rect.y = 494
                pygame.draw.rect(self.image, (255, 0, 0), [0, 0, Box.WIDTH, Box.HEIGHT], 2)
            elif 11 <= pos <= 19:
                print("pos 11:21: {0}".format(pos))
                self.image = pygame.Surface([Box.HEIGHT, Box.WIDTH])
                self.image.fill((255, 255, 255))
                self.image.set_colorkey((255, 255, 255))
                self.rect = self.image.get_rect()
                self.rect.x = 501 - ((Box.HEIGHT - 30 - 1) * 11)
                self.rect.y = 479 - ((Box.WIDTH - 1) * (pos - 10))
                pygame.draw.rect(self.image, (0, 255, 0), [0, 0, Box.HEIGHT, Box.WIDTH], 2)
            elif 20 <= pos <= 29:
                print("pos 21:31: {0}".format(pos))
                self.image = pygame.Surface([Box.WIDTH, Box.HEIGHT])
                self.image.fill((255, 255, 255))
                self.image.set_colorkey((255, 255, 255))
                self.rect = self.image.get_rect()
                self.rect.x = 32 + ((Box.WIDTH - 1) * (pos - 20))
                self.rect.y = 16
                pygame.draw.rect(self.image, (0, 255, 0), [0, 0, Box.WIDTH, Box.HEIGHT], 2)
            elif 30 <= pos <= 40:
                print("pos 21:31: {0}".format(pos))
                self.image = pygame.Surface([Box.HEIGHT, Box.WIDTH])
                self.image.fill((255, 255, 255))
                self.image.set_colorkey((255, 255, 255))
                self.rect = self.image.get_rect()
                self.rect.x = 496
                self.rect.y = 31 + ((Box.WIDTH - 1) * (pos - 30))
                pygame.draw.rect(self.image, (0, 0, 255), [0, 0, Box.HEIGHT, Box.WIDTH], 2)

        else:
            print("mod 10: {0}".format(pos))
            self.image = pygame.Surface([Box.WIDTH + 30, Box.HEIGHT])
            self.image.fill((255, 255, 255))
            self.image.set_colorkey((255, 255, 255))

            if 0 <= pos <= 10:
                self.rect = self.image.get_rect()
                self.rect.x = 496 - ((Box.WIDTH + 3 - 1) * pos)
                self.rect.y = 494
                pygame.draw.rect(self.image, (0, 0, 0), [0, 0, Box.WIDTH + 30, Box.HEIGHT], 2)

            elif 20 <= pos <= 31:
                self.rect = self.image.get_rect()
                self.rect.x = 18 + ((Box.WIDTH + 3 - 1) * (pos - 20))
                self.rect.y = 16
                pygame.draw.rect(self.image, (255, 0, 0), [0, 0, Box.WIDTH + 30, Box.HEIGHT], 2)

        self.rect.center = (self.rect.x + 1024 / 4, self.rect.y + 600/13)

    def on_init(self):
        super().on_init()

    def on_event(self, event):
        super().on_event(event)

    def on_loop(self):
        super().on_loop()

    def on_render(self, screen):
        super().on_render(screen)
            # ---Solution 2---
            # Just draw the non-filled rect here.

        #self.screen.blit(self.image, self.rect)



    def on_cleanup(self):
        super().on_cleanup()

