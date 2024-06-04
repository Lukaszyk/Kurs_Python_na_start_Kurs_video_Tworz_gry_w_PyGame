import pygame

pygame.init()
WIN = pygame.display.set_mode((1200,800)) #nadanie rozmiaru okna
WIN.fill('blue') #wypełnienie

x = 70

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


    WIN.fill('blue') #wypełnienie
    #wczytanie pliku graficznego do projektu
    GRAFIKA = pygame.image.load('Kurs_Python_na_start_Kurs_video_Tworz_gry_w_PyGame\img\T.png')
    WIN.blit(GRAFIKA, (x, 300)) #umieszczenie obiektu w oknie

    x = x + 1

    pygame.time.wait(100)

    pygame.draw.line(WIN, 'yellow', (45, 70), (45, 200), 6) 
    '''
    1: surface to wskazanie, w którym oknie mamy rysować,
    2: color kolor 
    3: start_pos (x - początek, y - początek), 
    4: end_pos (x - koniec, y - koniec), 
    5: width grubość rysowanego obiektu ''' 

    pygame.draw.circle(WIN, 'red', (120, 150), 30, 6) #okrąg
    pygame.draw.rect(WIN, 'green', (0, 0, 100, 50), 6) #prostokąt
    pygame.draw.polygon(WIN, 'pink', [(70, 80), (40, 90), (150, 180)], 6) #wielokąt

    pygame.display.update() #aktualizacja wyświetlania


