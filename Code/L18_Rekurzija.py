#
# L18_Rekurzija
#

# Ukljuci biblioteku pygame
import pygame

# Definiraj boje
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def recursive_draw(x, y, width, height):
    # Rekurzivno crtanje pravokutnika
    pygame.draw.rect(screen, BLACK,[x, y, width, height], 1)
    # Ako je širina pravokutnika veća od 14 smanji ju
    if(width > 14):
        # Smanji dimenzije
        x += width * .1
        y += height * .1
        width *= .8
        height *= .8
        # Ponovo pozovi funkciju rekurzivno
        recursive_draw(x, y, width, height)

# Inicijaliziraj pygame
pygame.init()

# Postavi dimenzije ekrana
size = [700, 500]
screen = pygame.display.set_mode(size)

# Postavi naslov prozora 
pygame.display.set_caption("Rekurzija")
 
# Postavi varijablu za kraj programa
done = False
 
# Postavi varijablu za brzinu osvjezavanja ekrana
clock = pygame.time.Clock()

# Gavna petlja 
while not done:
    # Procitaj akciju igraca
    for event in pygame.event.get():
        # Ako je igrac kliknuo na kruzic zavrsi program
        if event.type == pygame.QUIT:
            done = True
        # Postavi pozadinu prozora
        screen.fill(WHITE)
        # Pozovi funkciju za crtanje pravokutnika
        recursive_draw(0, 0, 700, 500)
        # Obnovi prikaz na ekranu
        pygame.display.flip()
        # Postavi osvjezivanje ekrana na 60 fps
        clock.tick(60)

# zatvori pygame
pygame.quit()


