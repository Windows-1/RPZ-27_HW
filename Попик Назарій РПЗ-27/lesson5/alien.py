import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Клас одного прибульця з флоту"""

    def __init__(self, ai_game):
        """Додає прибульця на його стартову позицію"""

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #Set starting position(paddings from the left and top)
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x) #virtual position

    def check_edges(self):
        """Повертає True якщо прибулець торкнувся краю"""

        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
