import pygame
import Colors


TILE_SIZE = 25
FPS = 60  # Frames Per Second
MPS = 3   # Munches Per Second

class Pacman(pygame.sprite.Sprite):
  def __init__(self, center):
    super(Pacman, self).__init__()
    self.surf = pygame.Surface((TILE_SIZE, TILE_SIZE))
    self.rect = self.surf.get_rect(center = center)
    self.mouth_size = 0
    self.frame = 0

  def update(self):
    self.mouth_size = ((FPS / (MPS * 2)) - abs(self.frame % (FPS / MPS) - (FPS / (MPS * 2)))) / (FPS / MPS)
    self.frame += 1

  def draw(self):
    pygame.draw.circle(self.surf, Colors.YELLOW, (TILE_SIZE / 2, TILE_SIZE / 2), TILE_SIZE * 0.4)
    pygame.draw.polygon(self.surf, Colors.CLEAR, [
      (TILE_SIZE / 2, TILE_SIZE / 2),
      (TILE_SIZE, (TILE_SIZE / 2) - (TILE_SIZE * self.mouth_size)),
      (TILE_SIZE, (TILE_SIZE / 2) + (TILE_SIZE * self.mouth_size))
    ])
    self.surf = pygame.transform.rotate(self.surf, 90)
