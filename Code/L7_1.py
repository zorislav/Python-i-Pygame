#
# L7_1
#

# Importiraj biblioteku funkcija Pygame
import pygame

# Inicijaliziraj game engine
pygame.init()

# Definiraj boje
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = ( 255, 0, 0)
BLUE = (0, 0, 255)

# Postavi veličinu prozora
size = (500, 500)
screen = pygame.display.set_mode(size)

# Varijabla koja označava kad završavamo program
done = False
# Varijabla koja prati brzinu izvršavanja programa
clock = pygame.time.Clock()

# Pocetna pozicija cetverokuta
rect_x = 50
rect_y = 50
# Brzina i smjer cetverokuta
rect_change_x = 5
rect_change_y = 5

# Glavna petlja
while not done:
    # Petlja glavnog eventa
    for event in pygame.event.get():         # Hvatanje akcije igrača
        if event.type == pygame.QUIT: # Igrač je pritisnuo close window
            done = True # postavljamo varijablu za kraj programa

    # Postavi boju ekrana na bijelo
    screen.fill(BLACK)

    # Nacrtaj pravokutnik od (rect_x, rect_y) sirine 50 visine 50
    pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 50, 50])

    # Promijeni koordinate gornjeg lijevog vrha
    rect_x += rect_change_x
    rect_y += rect_change_y

    # Odbijanje pravokutnika ako je potrebno
    if rect_y > 450 or rect_y < 0:
        rect_change_y = rect_change_y * -1
    if rect_x > 450 or rect_x < 0:
        rect_change_x = rect_change_x * -1

    # Ažuriranje ekrana
    pygame.display.flip()    
    # Postavi limit na 60 FPS
    clock.tick(60)

# Po izlasku iz petlje zatvori ekran
pygame.quit()
