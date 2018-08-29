import pygame
import pygame.gfxdraw


class TestSurf:
    N_PLAYERS = 2

    def __init__(self) -> None:
        super().__init__()
        pygame.init()
        self.size = self.weight, self.height = 1024, 680
        self.surface = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)

        self.other_surface = pygame.Surface((800, 800))
        self.other_surface_rect = self.other_surface.get_rect(topleft=(100, 0))
        self.other_surface = self.other_surface.convert()
        self.other_surface.fill((50, 0, 0))

        self.player_circles = []

        for i in range(TestSurf.N_PLAYERS):
            player_circle = {'surf': pygame.Surface((50, 50), pygame.SRCALPHA), 'rect': None, 'click_rect': None}
            rect = player_circle['surf'].get_rect()
            rect.x = 600
            rect.y = 30 + (100 * i)
            click_rect = pygame.rect.Rect((700, 30 + (100 * i), 50, 50))
            player_circle['rect'] = rect
            player_circle['click_rect'] = click_rect
            self.player_circles.append(player_circle)
            pygame.gfxdraw.aacircle(self.player_circles[i]['surf'], 25, 25, 20, (0, 0, 0))
            pygame.gfxdraw.filled_circle(self.player_circles[i]['surf'], 25, 25, 20, (0, 255, 0))
            self.other_surface.blit(self.player_circles[i]['surf'], self.player_circles[i]['rect'])

        self.surface.blit(self.other_surface, self.other_surface_rect)

    def on_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                for circle_pos in self.player_circles:
                    if circle_pos['click_rect'].collidepoint(pos):
                        pygame.draw.rect(self.other_surface, (0, 0, 0), circle_pos['rect'], 1)

    def on_render(self, screen):
        screen.fill((200, 0, 0))
        screen.blit(self.other_surface, self.other_surface_rect)


if __name__ == "__main__":
    clock = pygame.time.Clock()
    test_surf = TestSurf()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            test_surf.on_event(event)
        test_surf.on_render(test_surf.surface)
        pygame.display.flip()
        clock.tick(60)





