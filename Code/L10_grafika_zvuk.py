#
# L10_grafika_zvuk 
#

# Importiraj biblioteku funkcija Pygame
import pygame

# Inicijaliziraj game engine
pygame.init()

# Definiraj boje
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)

# Postavi veličinu prozora
size = (800, 600)
screen = pygame.display.set_mode(size)

# Ucitaj sliku za pozadine
background_image = pygame.image.load("L10_saturn_family1.jpg").convert()

# Postavi koordinate za crtanje pozadine
background_position = [0, 0]

# Ucitaj sliku koju ce igrac pomicati
player_image = pygame.image.load("L10_playerShip1_orange.png").convert()
# Ne prikazuj crnu boju na slici kiju pomice igrac
player_image.set_colorkey(BLACK)

# Ucitaj datoteku sa zvukom
click_sound = pygame.mixer.Sound("L10_laser5.ogg")

# varijabla koja prati brzinu izvršavanja programa
clock = pygame.time.Clock()

# Varijabla koja označava kad završavamo program
done = False

# Glavna petlja
while not done:
    # Petlja glavnog eventa
    for event in pygame.event.get():         # Hvatanje akcije igrača
        if event.type == pygame.QUIT: # Igrač je pritisnuo close window
            done = True # postavljamo varijablu za kraj programa
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # kad igrac pritisne tipku na misu pusti zvuk
            click_sound.play()
                  
    # Postavi pozadinsku grafiku na screen
    screen.blit(background_image, background_position)

    # Procitaj koordinate misa
    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]

    # nacrtaj sliku igraca na poziciji misa
    screen.blit(player_image, [x, y])

    # Ažuriranje ekrana
    pygame.display.flip()    
    # Postavi limit na 60 FPS
    clock.tick(20)

# Po izlasku iz petlje zatvori ekran
pygame.quit() 




