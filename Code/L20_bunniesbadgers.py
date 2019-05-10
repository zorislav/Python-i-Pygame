#
# L20_bunniesbadgers.py
#

# 1 - Ukljuci dodatne module
import pygame
# Eksplicitno ukljuci konstante iz pygame namespace-a
from pygame.locals import *
# Ukljuci biblioteku math
import math
# Ukljuci biblioteku random
import random
# Ukljuci biblioteku sys
import sys

# 2 - Osnovne postavke
# Inicijaliziraj pygame
pygame.init()
# Postavi naslov prozora
pygame.display.set_caption('Bunnies and Badgers')
# Definiraj velicinu prozora igrice
width, height = 640, 480
screen=pygame.display.set_mode((width, height))
# Polje za spremanje informacije o pritisnutim tipkama
keys = [False, False, False, False]
# Zekina pozicija
playerpos=[100,250]
# Da li izvrsavamo program 0=ne 1=Da
running = 1
# Nacin zavrsetka programa 0=poraz 1=pobjeda
exitcode = 0
# Brojac pogodjenih dabrova i ispaljenih strelica
acc = [0,0]
# Info o strelicama
# Za svaku strelicu: Kut izmedju zeke i pozicije misa, x kooordinata zeke, y koordinata zeke
arrows = []
# Info o jazavcima
# Vrijeme do kreiranja novog kazavca, umanjuje se za 1 za svaki frame
badtimer=100
# Frekvancija kreiranja novih jazavaca
badtimer1=0
# Početne koordinate jazavca
badguys=[[640,100]]
healthvalue=194

# 3 - Ucitaj likove
# Zeko
player = pygame.image.load("L20_dude.png")
# Dvorac
castle = pygame.image.load("L20_castle.png")
# Trava
grass = pygame.image.load("L20_grass.png")
# Strelica
arrow = pygame.image.load("L20_bullet.png")
# Jazavac
badguyimg1 = pygame.image.load("L20_badguy.png")
badguyimg=badguyimg1
# Stupac energije i energija
healthbar = pygame.image.load("L20_healthbar.png")
health = pygame.image.load("L20_health.png")
# Kraj igre i pobjeda
gameover = pygame.image.load("L20_gameover.png")
youwin = pygame.image.load("L20_youwin.png")

# 3.1 - Ucitaj zvuk
hit = pygame.mixer.Sound("L20_explode.wav")
enemy = pygame.mixer.Sound("L20_enemy.wav")
shoot = pygame.mixer.Sound("L20_shoot.wav")
hit.set_volume(0.05)
enemy.set_volume(0.05)
shoot.set_volume(0.05)
pygame.mixer.music.load('L20_moonlight.wav')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.25)

# 4 - Glavna petlja programa
while running:
    # 5 - Obrisi ekran prije ponovnog crtanja
    screen.fill(0)

    # 6 - Crtanje elemenata ekrana
    # Nartaj travu - ponavljaj duz x i y osi ovsno o dimenzijama lika trave
    for x in range(int(width/grass.get_width())+1):
        for y in range(int(height/grass.get_height())+1):
            screen.blit(grass,(x*100,y*100))

    # Nacrtaj 4 dvorca
    screen.blit(castle,(0,30))
    screen.blit(castle,(0,135))
    screen.blit(castle,(0,240))
    screen.blit(castle,(0,345 ))

    # 6.1 Nacrtaj zeku
    # Procitaj poziciju misa
    position = pygame.mouse.get_pos()
    # Izracunaj kut izmedju zeke i misa
    angle = math.atan2(position[1]-(playerpos[1]),position[0]-(playerpos[0]))    
    # Pretvori kut iz radijana u stupnjeve
    playerrot = pygame.transform.rotate(player, 360-angle*57.29)
    # Nova pozicija zeke
    playerpos1 = (playerpos[0]-playerrot.get_rect().width/2, playerpos[1]-playerrot.get_rect().height/2)
    # Nacrtaj zeku na poziciji playerpos1
    screen.blit(playerrot, playerpos1)

    # 6.2 Crtanje strelica
    # za svaku strelicu iz polja arrows
    for bullet in arrows:
        index=0
        # Koordinate strelice
        velx=math.cos(bullet[0])*10 # Izracunaj novu x koordinatu
        vely=math.sin(bullet[0])*10 # Izracunaj novu y koordinatu
        # Azuriraj x i y koordinate strelice
        bullet[1]+=velx
        bullet[2]+=vely
        # Ako su koordinate strelice van ekrana, ukloni strelicu iz niza arrows 
        if bullet[1]<-64 or bullet[1]>640 or bullet[2]<-64 or bullet[2]>480:
            arrows.pop(index)
        # Idi na slijedeću strelicu
        index+=1
        # Za svaku strelicu iz pola arrows  
        for projectile in arrows:
            # Kreiraj slitu strelice zarotiranu za kut u arrows[0]
            arrow1 = pygame.transform.rotate(arrow, 360-projectile[0]*57.29)
            # Nacrtaj sliku zarotirane strelice na koordinatama arrows[1],arrows[2]
            screen.blit(arrow1, (projectile[1], projectile[2]))

    # 6.3 Crtanje jazavaca
    # Vrijeme tekuceg jazavca je isteklo, kreiraj novog
    if badtimer==0:
        badguys.append([640, random.randint(50,430)]) # koordinate x=640 50<y<430
        # Postavi vrijeme trajanja novog jazavca
        badtimer=100-(badtimer1*2)
        # Povecavaj frekvenciju kreiranja novih jazavaca do 7.
        if badtimer1>=35:
            badtimer1=35
        else:
            badtimer1+=5
    index=0
    # Za svakog jazavca
    for badguy in badguys:
        # Ako je jazavac isasao sa ekrana ukloni ga sa liste
        if badguy[0]<-64:
            badguys.pop(index)
        # Inace ga pomakni u lijevo za 7 pixela
        badguy[0]-=7
        # 6.3.1 - Jazavci napadaju dvorce
        # Prociraj dimenzije pravokutnika koji omedjuje sliku jazavca
        badrect=pygame.Rect(badguyimg.get_rect())
        # Procitaj x i y koordinate jazavca
        badrect.top=badguy[1]
        badrect.left=badguy[0]
        # Ako se jazavac sudario sa dvorcem (x<64), smanji energiju igraca i ukloni jazavca
        if badrect.left<64:
            healthvalue -= random.randint(5,20)
            badguys.pop(index)
            hit.play()
        #6.3.2 - Strelice ubijaju jazavce
        index1=0
        # Za svaku strelicu
        for bullet in arrows:
            # Prociraj dimenzije pravokutnika koji omedjuje sliku strelice
            bullrect=pygame.Rect(arrow.get_rect())
            # Procitaj x i y koordinate strelice
            bullrect.left=bullet[1]
            bullrect.top=bullet[2]
            # Ako se strelica i jazavac preklapaju
            if badrect.colliderect(bullrect):
                # Uvecaj brojac pogodjenih dabrova za 1
                acc[0]+=1
                # Ukloni tekuceg dabra i strelicu
                badguys.pop(index)
                arrows.pop(index1)
                enemy.play()
            index1+=1

        # 6.3.3 - Idi na slijedeceg jazavca
        index+=1
    # Prikazi sve jazavce na ekranu
    for badguy in badguys:
        screen.blit(badguyimg, badguy)

    # 6.4 - Nacrtaj sat
    # Definiraj font za sat
    font = pygame.font.Font(None, 24)
    # Definiraj tekst za ispis
    survivedtext = font.render("Time: "+'{:02d}'.format((90000-pygame.time.get_ticks())//1000)+" s", True, (0,0,0))
    # Procitaj dimenzije pravokutnika koji omedjuje tekst
    textRect = survivedtext.get_rect()
    # Postavi koordinate gornjeg desnog vrha pravokutnika za tekst
    textRect.topright=[635,5]
    # Nacrtaj tekst na ekranu
    screen.blit(survivedtext, textRect)

    # 6.5 - Prikazi energiju igraca
    # Prvo nacrtaj puni crveni stupac energije 
    screen.blit(healthbar, (5,5))
    # Zatim nacrtaj zeleni stupac preko crvenog ovisno o trenutnoj energiji igraca
    for health1 in range(healthvalue):
        screen.blit(health, (health1+8,8))

    # 7 - Azuriraj ekran
    pygame.display.flip()

    # 8 - Hvatanje akcije igraca
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Igrac je zatvorio prozor
            running = 0 # Kraj programa
        if event.type==pygame.MOUSEBUTTONDOWN: # Igrac je pritisnuo lijevu tipku misa
            # Procitaj poziciju misa
            position=pygame.mouse.get_pos()
            # Povecaj brojac ispaljenih strelica za 1
            acc[1]+=1
            # Za tekucu strelicu zapamti kut izmedju zeke i pozicije misa, x oordinatu zeke, y koordinatu zeke
            arrows.append([math.atan2(position[1]-(playerpos1[1]+32),position[0]-(playerpos1[0]+26)),playerpos1[0]+32,playerpos1[1]+32])
            shoot.play()
        if event.type == pygame.KEYDOWN: # Igrac je pritisnuo tipku
            if event.key==K_w:
                keys[0]=True
            elif event.key==K_a:
                keys[1]=True
            elif event.key==K_s:
                keys[2]=True
            elif event.key==K_d:
                keys[3]=True
        if event.type == pygame.KEYUP: # Igrac je otpustio tipku
            if event.key==pygame.K_w:
                keys[0]=False
            elif event.key==pygame.K_a:
                keys[1]=False
            elif event.key==pygame.K_s:
                keys[2]=False
            elif event.key==pygame.K_d:
                keys[3]=False

    # 9 - Pomakni zeku
    if keys[0]:
        playerpos[1]-=5
    elif keys[2]:
        playerpos[1]+=5
    if keys[1]:
        playerpos[0]-=5
    elif keys[3]:
        playerpos[0]+=5

    badtimer-=1            

    #10 - Provjera da li je igrac pobjedio ili izgubio
    # Ako je proslo 90s igra je zavrsena
    if pygame.time.get_ticks()>=90000:
        running=0
        exitcode=1
    # Ako je energija igraca pala na 0 izgubio je
    if healthvalue<=0:
        running=0
        exitcode=0
    # Azuriraj preciznost igraca    
    if acc[1]!=0:
        accuracy=acc[0]*1.0/acc[1]*100
    else:
        accuracy=0

# 11 - Zavrsni ekran win/lose        
if exitcode==0:
    # Poraz
    pygame.font.init()
    font = pygame.font.Font(None, 24)
    text = font.render("Accuracy: "+str(accuracy)+"%", True, (255,0,0))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery+24
    screen.blit(gameover, (0,0))
    screen.blit(text, textRect)
else:
    # Pobjeda
    pygame.font.init()
    font = pygame.font.Font(None, 24)
    text = font.render("Accuracy: "+str(accuracy)+"%", True, (0,255,0))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery+24
    screen.blit(youwin, (0,0))
    screen.blit(text, textRect)
    
# Petlja koja osigurva prikaz zavrsnog ekrana dok igrac ne zatvori prozor
while 1:
    # Uhvati akciju igraca    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Igrac je zatvorio prozor
            # Zavrsi program
            pygame.quit()
            sys.exit()
    # Azuriraj ekran
    pygame.display.flip()
