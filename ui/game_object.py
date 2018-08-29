import pygame


class GameObject(pygame.sprite.Sprite):

    def __init__(self) -> None:
        super(GameObject, self).__init__()

    def on_init(self, **kwargs):
        pass

    def on_event(self, event):
        pass

    def on_loop(self):
        pass

    def on_render(self, screen):
        pass

    def on_cleanup(self):
        pass