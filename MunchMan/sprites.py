from colours import CLEAR, YELLOW
from enum import Enum, auto
import pygame


TILE_SIZE = 25
FPS = 60  # Frames Per Second

class Pacman(pygame.sprite.Sprite):
  def __init__(self, center):
    super(Pacman, self).__init__()
    self.surf = pygame.Surface((TILE_SIZE, TILE_SIZE))
    self.rect = self.surf.get_rect(center = center)
    self.frames_per_loop = (FPS / 3)
    self.frame = 0

  def update(self):
    self.frame = (self.frame + 1) % self.frames_per_loop

  def draw(self):
    # Draw Pacman's body
    pygame.draw.circle(self.surf, YELLOW, (TILE_SIZE / 2, TILE_SIZE / 2), TILE_SIZE * 0.4)

    # Cut out the mouth triangle
    half_loop = self.frames_per_loop / 2
    mouth_size = half_loop - abs(self.frame - half_loop)
    mouth_y = TILE_SIZE * mouth_size / self.frames_per_loop
    pygame.draw.polygon(self.surf, CLEAR, [
      (TILE_SIZE / 2, TILE_SIZE / 2),
      (TILE_SIZE, (TILE_SIZE / 2) - mouth_y),
      (TILE_SIZE, (TILE_SIZE / 2) + mouth_y)
    ])

    # Face Pacman in the correct direction
    self.surf = pygame.transform.rotate(self.surf, 90)

class WallShape(Enum):
  Single = auto()   # Single dot with no adjacent walls.
  End = auto()      # An end with one adjacent wall piece,
                    # default joining at top.
  Corner = auto()   # An L shape, default like the letter L.
  Straight = auto() # A straight piece, default like letter I.
  Tee = auto()      # A tee piece, default upside down T.
  Cross = auto()    # A cross joining all four directions.
