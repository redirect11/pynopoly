import sys
import pygame

class Rect():
    def __init__(self, name, color, x, y):
        self.rect = pygame.Rect(10, 10, 10, 10)
        self.rect.x = x
        self.rect.y = y
        self.name = name
        self.color = color


class ColorPicker:
    def __init__(self, position):
        width, height = 400, 400
        self.all_rects = []
        self.selected_rect = None
        self.NAME_TO_RGBA = pygame.color.THECOLORS
        self.RGBA_TO_NAME = {}
        for name, rgb in self.NAME_TO_RGBA.items():
            if rgb in self.RGBA_TO_NAME:
                self.RGBA_TO_NAME[rgb].append(name)
            else:
                self.RGBA_TO_NAME[rgb] = [name]

        self.colors = self.NAME_TO_RGBA
        self.gridX = 25
        self.show = False
        self.position = position
        self.MakeGrid(position)

    def MakeGrid(self, position):
        x, y = position[0], position[1]
        i = 0
        for name, rgba in self.colors.items():
            self.all_rects.append(Rect(name, rgba, x, y))
            x += 10
            i += 1
            if i == 25:
                i = 0
                y += 10
                x = position[0]

    def on_render(self, surface):
        if self.show:
            for rect in self.all_rects:
                pygame.draw.rect(surface, rect.color, rect.rect)

    def on_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("clicked")
                pos = pygame.mouse.get_pos()
                print(pos)
                for rect in self.all_rects:
                    if rect.rect.collidepoint(pos):
                        print(rect.color)
                        self.selected_rect = rect
                        self.show = False

    def get_selected_color(self):
        return self.selected_rect.color

# while running:
#     clock.tick(60)
#
#     for e in pygame.event.get():
#
#     screen.blit(name_label, (100, 20))
#     screen.blit(color_label, (100, 40))
#
#     DrawWindow()