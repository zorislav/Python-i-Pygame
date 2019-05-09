#
# L9_mouse
#

# Importiraj biblioteku funkcija Pygame
import pygame

# Funkcija za crtanje objekta
def nacrtaj_covjeculjka(screen, x, y):
    # Glava
    pygame.draw.ellipse(screen, BLACK, [x-4,y-17,10,10], 0)
    # Noge
    pygame.draw.line(screen, BLACK, [x,y], [x+5,y+10], 2)
    pygame.draw.line(screen, BLACK, [x,y], [x-5,y+10], 2)
    # Tijelo
    pygame.draw.line(screen, RED, [x,y], [x,y-10], 2)
    # Ruke
    pygame.draw.line(screen, RED, [x,y-10], [x+4,y], 2)
    pygame.draw.line(screen, RED, [x,y-10], [x-4,y], 2)

# Inicijaliziraj game engine
pygame.init()

# Definiraj boje
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)

# Postavi veličinu prozora
size = (500, 500)
screen = pygame.display.set_mode(size)

# Varijabla koja označava kad završavamo program
done = False

# varijabla koja prati brzinu izvršavanja programa
clock = pygame.time.Clock()

# Sakrij kursor misa
pygame.mouse.set_visible(False)

# Postavi pocetne koordinate i pomake
kx = 100
ky = 100

# Glavna petlja
while not done:
    # Petlja glavnog eventa
    for event in pygame.event.get():         # Hvatanje akcije igrača
        if event.type == pygame.QUIT: # Igrač je pritisnuo close window
            done = True # postavljamo varijablu za kraj programa
            
    # Postavi boju ekrana na bijelo
    screen.fill(WHITE)

    # Dio koda za određuvanje pozicije mišem
    # Procitaj koordinate misa
    pos = pygame.mouse.get_pos()
    kx = pos[0]
    ky = pos[1]

    # nacrtaj objekt
    nacrtaj_covjeculjka(screen, kx, ky)

    # Ažuriranje ekrana
    pygame.display.flip()    
    # Postavi limit na 60 FPS
    clock.tick(20)

# Po izlasku iz petlje zatvori ekran
pygame.quit() 




