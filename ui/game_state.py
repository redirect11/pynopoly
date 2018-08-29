from ui.game_object import GameObject


class GameState(GameObject):
    STARTED = 1
    FIRST_ROLL = 2
    MOVING = 3
    MAIN_MENU = 4
    PLAYING = 5

    stateMap = {}

    def __init__(self, context) -> None:
        super().__init__()
        self.context = context

    def set_state(self, state, **kwargs):
        mapped_state = GameState.stateMap[state]
        self.context.set_state(mapped_state, **kwargs)
