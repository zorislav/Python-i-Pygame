#
# L12_Pokupi_blokove
#

# Ucitaj biblioteke
import pygame
import random
 
# Definiraj boje
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
 
class Block(pygame.sprite.Sprite):
    # Definicija klase koja predstavlja blokove
    # izvedena je iz klase Sprite Pygame libraryja
     
    def __init__(self, color, width, height):
        # Konstruktor prima boju i veličinu bloka
         
        # Pozovi konstruktor parent klase (Sprite)
        super().__init__()
 
        # Kreiraj i oboji blok
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        # Postavi koordinate prethodno definiranog pravokutnika
        # u varijablu rect - rect.x i rect.y
        self.rect = self.image.get_rect()
 
# Inicijaliziraj Pygame
pygame.init()
# Postavi dimenzije ekrana
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
 
# Definiraj listu svih blokova, kao listu objekata glase Group
block_list = pygame.sprite.Group()
 
# Definiraj listu svih sprajtova, kao listu objekata glase Group
all_sprites_list = pygame.sprite.Group()
 
for i in range(50):
    # Kreiraj blok
    block = Block(BLACK, 20, 15)
 
    # Postavi slucajne kordinate bloka
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)
 
    # Dodaj blok u listu blokova i sprajtova
    block_list.add(block)
    all_sprites_list.add(block)
 
# Kreiraj crveni blok za igraca
player = Block(RED, 20, 15)
all_sprites_list.add(player)
 
# Ponavljaj glavnu petlju dok igrac ne zatvori prozor
done = False
 
# Definiraj brzinu
clock = pygame.time.Clock()
 
score = 0
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
 
    # Obrisi ekran
    screen.fill(WHITE)
 
    # Procitaj koordinate misa
    pos = pygame.mouse.get_pos()
 
    # Preslikaj koodrinate misa u koordinate igracevog bloka
    player.rect.x = pos[0]
    player.rect.y = pos[1]
 
    # Provjeri da li se blok igraca sudara sa nekim drugim blokom
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)
 
    # Povecaj brojac sudara i ispisi na konzolu
    for block in blocks_hit_list:
        score += 1
        print(score)
 
    # Iscrtaj sve sprajtove na ekran
    all_sprites_list.draw(screen)
 
    # Osvjezi ekran
    pygame.display.flip()
 
    # Definiraj 60 fps
    clock.tick(60)
 
pygame.quit()
