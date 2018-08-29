from ui.game_object import GameObject

class PyGameProp(GameObject):

    def __init__(self, surface) -> None:
        super().__init__(surface)

    def on_init(self):
        super().on_init()

    def on_event(self, event):
        super().on_event(event)

    def on_loop(self):
        super().on_loop()

    def on_render(self, screen):
        super().on_render(screen)

    def on_cleanup(self):
        super().on_cleanup()


