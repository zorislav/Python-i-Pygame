#
# L7_2
#

# Importiraj biblioteke funkcija Pygame i random
import pygame
import random

# Inicijaliziraj game engine
pygame.init()

# Definiraj boje
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Postavi veličinu prozora
size = (500, 500)
screen = pygame.display.set_mode(size)

# Varijabla koja označava kad završavamo program
done = False
# Varijabla koja prati brzinu izvršavanja programa
clock = pygame.time.Clock()

# Kreiraj praznu listu pahuljica
snow_list = []
# Generiraj 50 pahuljica sa random x,y koordinatama
for i in range(50):
    x = random.randrange(0, 499)
    y = random.randrange(0, 499)
    snow_list.append([x, y])

# Glavna petlja
while not done:
    # Petlja glavnog eventa
    for event in pygame.event.get():         # Hvatanje akcije igrača
        if event.type == pygame.QUIT: # Igrač je pritisnuo close window
            done = True # postavljamo varijablu za kraj programa

    # Postavi boju ekrana na bijelo
    screen.fill(BLACK)

    # Procesiraj svaku pahuljicu iz liste
    for i in range(len(snow_list)):
        # Nacrtaj pahuljicu
        pygame.draw.circle(screen, WHITE, snow_list[i], 2)
        # Pomakni pahuljicu za 1 pixel dolje
        snow_list[i][1] += 1

        # Ako je pahuljica prosla dno ekrana
        if snow_list[i][1] > 499:
            # Postavi y koordinatu pahuljice ispod ekrana
            y = random.randrange(-50, -10)
            snow_list[i][1] = y
            # Postavi x koordinatu pahuljice
            x = random.randrange(0, 499)
            snow_list[i][0] = x

    # Ažuriranje ekrana
    pygame.display.flip()    

    # Postavi limit na 20 FPS
    clock.tick(20)

# Po izlasku iz petlje zatvori ekran
pygame.quit()

