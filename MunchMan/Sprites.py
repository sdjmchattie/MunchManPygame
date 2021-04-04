import pygame


class Pacman(pygame.sprite.Sprite):
  def __init__(self):
    super(Pacman, self).__init__()
    self.surf = pygame.Surface((25, 25))
    self.surf.fill((255, 255, 255))
    self.rect = self.surf.get_rect()

  def update(self):
    pass

  def draw(self):
    pass
