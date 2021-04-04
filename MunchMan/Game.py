import pygame
import Colors
import Sprites


SCREEN_WIDTH = 525
SCREEN_HEIGHT = 675

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pacman = Sprites.Pacman((SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

all_sprites = pygame.sprite.Group()
all_sprites.add(pacman)

running = True
while running:
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          running = False

  screen.fill(Colors.DARK_GREY)

  for sprite in all_sprites:
    sprite.update()
    sprite.draw()
    screen.blit(sprite.surf, sprite.rect)

  pygame.display.flip()
  clock.tick(60)

pygame.quit()
