#
# l4.py
#
# Importiraj biblioteku funkcija Pygame
import pygame
# Inicijaliziraj game engine
pygame.init()
# Definiraj boje i broj PI
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = ( 255, 0, 0)
BLUE = (0, 0, 255)
PI = 3.141592653

# Postavi veličinu prozora
size = (400, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Moja igrica")

# Varijabla koja označava kad završavamo program
done = False
# varijabla koja prati brzinu izvršavanja programa
clock = pygame.time.Clock()

# Glavna petlja
while not done:
    # Petlja glavnog event
    for event in pygame.event.get(): # Hvatanje akcije igrača
        if event.type == pygame.QUIT: # Igrač je pritisnuo close window
            done = True # postavljamo varijablu za kraj programa
    # Postavi boju ekrana na bijelo
    screen.fill(WHITE)
    # Nacrtaj liniju od (0,0) do (100,100) sirine 5 pixela
    pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)    

    # Nacrtaj pravokutnik od (20, 20) sirine 250 visine 200 debljine linije 2 
    pygame.draw.rect(screen, BLACK, [20, 20, 250, 100], 2)

    # Nacrtaj elipsu unutar prethodnog pravokutnika
    pygame.draw.ellipse(screen, BLACK, [20, 20, 250, 100], 2)

    # Nacrtaj luk centar u (20,220) širina 250, visina 200, početni kut 0 , zavrsni kut PI/2
    # debljina linije 2
    pygame.draw.arc(screen, BLACK, [20, 220, 250, 200], 0, PI/2, 2)

    # Nacrtaj trokut izmedju tocaka (100,100) (0,200) (200,200) crne boje i debljine linije 5
    pygame.draw.polygon(screen, BLACK, [[100, 100], [0, 200], [200, 200]], 5) 

    # Nacrtaj tekst "Moj tekst", font Colibri, velicina 25, boja crna, bold, ne italic,
    # anti-aliasing
    font = pygame.font.SysFont("Calibri", 25, True, False)
    text = font.render("Moj tekst", True, BLACK)
    screen.blit(text, [250, 250])

    # Ažuriranje ekrana
    pygame.display.flip()    
    # Postavi limit na 60 FPS
    clock.tick(60)

# Po izlasku iz petlje zatvori ekran
pygame.quit() 


