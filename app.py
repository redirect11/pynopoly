import pygame
from pygame.locals import *

class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 1024, 680
        self._state = None

    def on_init(self):
        pygame.init()
        pygame.font.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self, screen):
        pass

    def on_cleanup(self):
        pygame.quit()

    def get_screen(self):
        return self._display_surf

    def set_state(self, state, **kwargs):
        self._state = state
        self._state.on_init(**kwargs)

    @property
    def state(self):
        return self._state

    def on_execute(self):
        clock = pygame.time.Clock()
        if not self.on_init():
            self._running = False

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render(self._display_surf)
            clock.tick(60)
        self.on_cleanup()



