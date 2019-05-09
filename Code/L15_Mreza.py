#
# L15_Mreza
#
import pygame
 
# Definiraj boje
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
# Postavi WIDTH and HEIGHT za svaku kockicu
WIDTH = 20
HEIGHT = 20
 
# Postavi razmak izmedju kockica
MARGIN = 5
 
# Kreiraj matricu koja sadrzi 10x10 kockica bijele boje
# 0 oznacava kockicu bijele a 1 zelene boje
grid = []
for row in range(10):
    # Dodaj prazan niz koji će sadržavati kockice u redu
    grid.append([])
    for column in range(10):
        # U prazan niz upisi po jednu nulu za svaki stupac 
        grid[row].append(0)   
 
# Kockicu u redu 2 i stupcu 6 postavi na zeleno
grid[1][5] = 1
 
# Inicijaliziraj pygame
pygame.init()
 
# Postavi dimenzije prozora
WINDOW_SIZE = [255, 255]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Postavi naslov prozora
pygame.display.set_caption("Mreza")
 
# Varijabla za izlaz iz glavne petlje
done = False
 
# varijabla za brzinu obnavljanja ekrana
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # Uhvati akciju igraca
        if event.type == pygame.QUIT:  # Igrac je kliknuo na close
            done = True  # Oznaci da zavrsavamo petlju
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Igrac je kliknuo. Procitaj poziciju misa
            pos = pygame.mouse.get_pos()
            # Pretvori koordinate misa u kockice matrice
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            # Oznaci da se kockica treba obojati u zeleno
            grid[row][column] = 1
            # Ispisi na konzoli koodrinate misa i poziciju kockice u matrici
            print("Click ", pos, "Grid coordinates: ", row, column)
 
    # Oboji screen u crno
    screen.fill(BLACK)
 
    # Nacrtaj matricu
    for row in range(10):
        for column in range(10):
            color = WHITE
            if grid[row][column] == 1:
                color = GREEN
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH, HEIGHT])
 
    # Postavi brzinu obnavljanja ekrana na 60fps
    clock.tick(60)
 
    # Obnovi prozor
    pygame.display.flip()
 
# Kraj programa
pygame.quit()
