import pygame
import Sprites


CLEAR = (0, 0, 0, 0)
DARK_GREY = (20, 20, 20)

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([525, 675])

pacman = Sprites.Pacman()

all_sprites = pygame.sprite.Group()
all_sprites.add(pacman)

running = True
while running:
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          running = False

  screen.fill(DARK_GREY)
  pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
  pygame.display.flip()
  clock.tick(60)

pygame.quit()
