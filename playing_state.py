from ui.game_state import GameState
from ui.py_game_board import PyGameBoard
from engine.game_controller import GameController


class PlayingState(GameState):
    def __init__(self, context, py_game_board: PyGameBoard) -> None:
        super().__init__(context)
        self.gameboard = py_game_board
        self.game_controller = GameController()

    def process_kwargs(self, kwargs):
        """Various optional customization you can change by passing kwargs."""
        settings = {"n_players" : None}
        for kwarg in kwargs:
            if kwarg in settings:
                settings[kwarg] = kwargs[kwarg]
            else:
                raise AttributeError("PlayingState has no keyword: {}".format(kwarg))
        self.__dict__.update(settings)

    def on_init(self, **kwargs):
        super().on_init()
        self.process_kwargs(kwargs)
        self.gameboard.on_init(**kwargs)

    def on_event(self, event):
        super().on_event(event)
        self.gameboard.on_event(event)

    def on_loop(self):
        super().on_loop()

    def on_render(self, screen):
        super().on_render(screen)
        self.gameboard.on_render(screen)

    def on_cleanup(self):
        super().on_cleanup()

