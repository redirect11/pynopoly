import pygame
from ui.py_game_board import PyGameBoard
from ui.game_state import GameState
from started_state import StartedState
from playing_state import PlayingState
from app import App


class PyNopoly(App):

    def __init__(self):
        super().__init__()

    def on_init(self):
        super().on_init()
        print("starting...")
        self.gameboard = PyGameBoard("images/bg.jpg")
        starting_state = StartedState(self)
        playing_state = PlayingState(self, self.gameboard)
        GameState.stateMap[GameState.STARTED] = starting_state
        GameState.stateMap[GameState.PLAYING] = playing_state
        self.set_state(starting_state)
        return True

    def on_event(self, event):
        super().on_event(event)
        #self.get_screen().fill((225, 225, 225))
        self.state.on_event(event)

    def on_loop(self):
        super().on_loop()
        self.state.on_loop()

    def on_render(self, screen):
        super().on_render(screen)
        self.state.on_render(screen)
        pygame.display.flip()

    def on_cleanup(self):
        super().on_cleanup()
        self.state.on_cleanup()


if __name__ == "__main__":
    theApp = PyNopoly()
    theApp.on_execute()
