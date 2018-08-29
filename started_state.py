import pygame
import pygameMenu
import pygame.gfxdraw
import pygameMenu.config_menu as _cfg
from ui.widgets.pg_button import PgButton
from ui.widgets.color_picker import ColorPicker
from pygameMenu.locals import *
from ui.game_state import GameState
from ui.widgets.pygame_textinput import TextBox

# TODO does it better to use player class or pygameplayer class (should be decoupled from Box class) directly

class StartMenu(pygameMenu.Menu):

    def __init__(self, surface, window_width, window_height, font, title, bgfun=None,
                 color_selected=_cfg.MENU_SELECTEDCOLOR, dopause=True, draw_region_x=_cfg.MENU_DRAW_X,
                 draw_region_y=_cfg.MENU_DRAW_Y, draw_select=_cfg.MENU_SELECTED_DRAW, enabled=True,
                 font_color=_cfg.MENU_FONT_COLOR, font_size=_cfg.MENU_FONT_SIZE,
                 font_size_title=_cfg.MENU_FONT_SIZE_TITLE, font_title=None, joystick_enabled=True,
                 menu_alpha=_cfg.MENU_ALPHA, menu_centered=_cfg.MENU_CENTERED_TEXT, menu_color=_cfg.MENU_BGCOLOR,
                 menu_color_title=_cfg.MENU_TITLE_BG_COLOR, menu_height=_cfg.MENU_HEIGHT, menu_width=_cfg.MENU_WIDTH,
                 onclose=None, option_margin=_cfg.MENU_OPTION_MARGIN, option_shadow=_cfg.MENU_OPTION_SHADOW,
                 rect_width=_cfg.MENU_SELECTED_WIDTH, title_offsetx=0, title_offsety=0):
        super().__init__(surface, window_width, window_height, font, title, bgfun, color_selected, dopause,
                         draw_region_x, draw_region_y, draw_select, enabled, font_color, font_size, font_size_title,
                         font_title, joystick_enabled, menu_alpha, menu_centered, menu_color, menu_color_title,
                         menu_height, menu_width, onclose, option_margin, option_shadow, rect_width, title_offsetx,
                         title_offsety)
        self._dopause = dopause

    def disablepause(self):
        self._dopause = False


class StartedState(GameState):

    COLOR_BACKGROUND = (128, 0, 128)
    COLOR_BLACK = (0, 0, 0)
    COLOR_WHITE = (255, 255, 255)
    MENU_BACKGROUND_COLOR = (200, 0, 0)
    WINDOW_SIZE = (1024, 600)

    COLOR_BLUE = (12, 12, 200)
    HELP = ['Press ESC to enable/disable Menu',
            'Press ENTER to access a Sub-Menu or use an option',
            'Press UP/DOWN to move through Menu',
            'Press LEFT/RIGHT to move through Selectors']
    N_PLAYERS = [2]

    def __init__(self, context) -> None:
        super().__init__(context)
        # Main menu, pauses execution of the application
        self.surface = context.get_screen()
        self.text_input = []
        self.player_names = {}
        self.name_labels = []
        self.font = pygame.font.Font("resources/fonts/MotionControl-Bold.otf", 48)
        surface = self.surface
        # self.other_surface = pygame.Surface((800, 800))
        # self.other_surface_rect = self.other_surface.get_rect(topleft=(100, 0))
        # self.other_surface = self.other_surface.convert()
        # self.other_surface.fill((50, 0, 0))
        
        self.active_text_box = 0
        self.start_button = PgButton((760, 580, 240, 80), (0, 10, 230), self.on_start_button_clicked,
                                     font=self.font, text="Start Playing")
        self.player_circles = []
        self.color_picker = ColorPicker((750, 100))
        pygame.display.flip()

        # declaring here because TextMenu doesn't recognize MethodType
        def main_background():
            """
            Background color of the main menu, on this function user can plot
            images, play sounds, etc.
            """
            surface.fill((0, 0, 0))

        def choose_names():
            a = StartedState.N_PLAYERS[0]
            print(a)
            surface.fill((200, 0, 0))
            for i in range(a):
                left = 350
                top = 30 + (100 * i)
                text_box = TextBox((left, top, 300, 60), id=i, command=self.handle_input,
                                   clear_on_enter=False, inactive_on_enter=False, font=self.font)
                if i > 0:
                    text_box.active = False
                self.text_input.append(text_box)
                self.name_labels.append(self.font.render("Player {0}".format(i+1), True, (255, 255, 255)))
                player_circle = {'surf': pygame.Surface((50, 50), pygame.SRCALPHA), 'rect': None}
                rect = player_circle['surf'].get_rect()
                rect.x = 680
                rect.y = 30 + (100 * i)
                player_circle['rect'] = rect
                self.player_circles.append(player_circle)

                self.surface.blit(self.name_labels[i], (((self.name_labels[i].get_width() + 200) // 2),
                                                              (5 + self.name_labels[i].get_height() // 2) + (100 * i)))
                pygame.gfxdraw.aacircle(self.player_circles[i]['surf'], 25, 25, 20, (0, 0, 0))
                pygame.gfxdraw.filled_circle(self.player_circles[i]['surf'], 25, 25, 20, (0, 255, 0))
                pygame.draw.rect(self.surface, (0, 0, 0), self.player_circles[i]['rect'], 1)
                self.surface.blit(self.player_circles[i]['surf'], self.player_circles[i]['rect'])

            self.menu.disablepause()
            self.menu.disable()
            self.menu.reset(1)

        self.menu = StartMenu(surface,
                              bgfun=main_background,
                              dopause=True,
                              color_selected=StartedState.COLOR_WHITE,
                              font=pygameMenu.fonts.FONT_BEBAS,
                              font_color=StartedState.COLOR_BLACK,
                              font_size=30,
                              menu_alpha=100,
                              menu_color=StartedState.MENU_BACKGROUND_COLOR,
                              menu_height=int(StartedState.WINDOW_SIZE[1] * 0.8),
                              menu_width=int(StartedState.WINDOW_SIZE[0] * 0.8),
                              onclose=PYGAME_MENU_CLOSE,
                              option_shadow=False,
                              title='PyNopoly',
                              window_height=StartedState.WINDOW_SIZE[1],
                              window_width=StartedState.WINDOW_SIZE[0]
                              )
        # menu.add_option(timer_menu.get_title(), timer_menu)  # Add timer submenu
        # menu.add_option(help_menu.get_title(), help_menu)  # Add help submenu
        # menu.add_option(about_menu.get_title(), about_menu)  # Add about submenu

        self.menu.add_option('Start', choose_names)
        self.menu.add_selector('N. Giocatori', [('2', 2),
                                                ('3', 3),
                                                ('4', 4),
                                                ('5', 5),
                                                ('6', 6)],
                               onreturn=None,
                               onchange=StartedState.change_n_players)
        self.menu.add_option('Exit', PYGAME_MENU_EXIT)  # Add exit function

    @staticmethod
    def change_n_players(n_players):
        StartedState.N_PLAYERS[0] = n_players
        print(StartedState.N_PLAYERS[0])

    def on_event(self, event):
        super().on_event(event)
        self.menu.mainloop(pygame.event.get())
        if self.menu.is_disabled():
            self.color_picker.on_event(event)
            self.start_button.check_event(event)
            for text_input in self.text_input:
                text_input.get_event(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    for circle_pos in self.player_circles:
                        if circle_pos['rect'].collidepoint(pos):
                            self.color_picker.show = True
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER, pygame.K_TAB):
                    self.text_input[self.active_text_box].active = False
                    if self.active_text_box == (len(self.text_input) - 1):
                        self.active_text_box = 0
                    else:
                        self.active_text_box = self.active_text_box + 1
                    self.text_input[self.active_text_box].active = True
            for i in range(len(self.text_input)):
                if self.text_input[i].active:
                    self.active_text_box = i

    def on_loop(self):
        super().on_loop()
        #for player_circle in self.player_circles:
        for text_input in self.text_input:
            text_input.update()

    def on_render(self, screen):
        super().on_render(screen)
        #screen.fill((200, 0, 0))
        for text_input in self.text_input:
            text_input.draw(screen)
        self.color_picker.on_render(screen)
        self.start_button.update(screen)

    def on_cleanup(self):
        super().on_cleanup()

    def handle_input(self, id, text):
        print("id {0} text {1}".format(id, text))
        self.player_names[id] = text

    def on_start_button_clicked(self):
        self.set_state(GameState.PLAYING, n_players=self.player_names)


