#
# L9_keyboard
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
x_pomak = 0
y_pomak = 0

joystick_count = pygame.joystick.get_count()
if joystick_count == 0:
    # No joysticks!
    print("Error, I didn't find any joysticks.")

# Glavna petlja
while not done:
    # Petlja glavnog eventa
    for event in pygame.event.get():         # Hvatanje akcije igraca
        if event.type == pygame.QUIT: # Igrač je pritisnuo close window
            done = True # postavljamo varijablu za kraj programa
        # Igrac je pritisnuo tipku
        elif event.type == pygame.KEYDOWN:
            # Pritisnuo je strelicu lijevo
            if event.key == pygame.K_LEFT: 
                # Pomakni covjeculjka 3 pixela lijevo
                x_pomak = -3
            # Pritisnuo je strelicu desno
            elif event.key == pygame.K_RIGHT: 
                # Pomakni covjeculjka 3 pixela desno
                x_pomak = 3 
            # Pritisnuo je strelicu gore
            elif event.key == pygame.K_UP: 
                # Pomakni covjeculjka 3 pixela gore
                y_pomak = -3 
            # Pritisnuo je strelicu dolje
            elif event.key == pygame.K_DOWN: 
                # Pomakni covjeculjka 3 pixela dolje
                y_pomak = 3 
        # Igrac je otpustio tipku
        elif event.type == pygame.KEYUP:
            # Otpustio je strelicu lijevo ili desno
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: 
                # Ponisti horizontalni pomak covjeculjka
                x_pomak = 0
            # Otpustio je strelicu gore ili dolje
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                # Ponisti vertikalni pomak covjeculjka
                y_pomak = 0

    # Promjeni koordinate
    kx += x_pomak
    ky += y_pomak
                
    # Postavi boju ekrana na bijelo
    screen.fill(WHITE)

    # nacrtaj objekt
    nacrtaj_covjeculjka(screen, kx, ky)

    # Ažuriranje ekrana
    pygame.display.flip()    
    # Postavi limit na 60 FPS
    clock.tick(20)

# Po izlasku iz petlje zatvori ekran
pygame.quit() 




