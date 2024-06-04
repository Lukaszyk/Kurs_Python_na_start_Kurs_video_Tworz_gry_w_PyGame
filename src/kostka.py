import random
import pygame

pygame.init()

WIN = pygame.display.set_mode((300, 300))

file_list = ['Kurs_Python_na_start_Kurs_video_Tworz_gry_w_PyGame/img/1.png', 'Kurs_Python_na_start_Kurs_video_Tworz_gry_w_PyGame/img/2.png', 'Kurs_Python_na_start_Kurs_video_Tworz_gry_w_PyGame/img/3.png', 'Kurs_Python_na_start_Kurs_video_Tworz_gry_w_PyGame/img/4.png', 'Kurs_Python_na_start_Kurs_video_Tworz_gry_w_PyGame/img/5.png', 'Kurs_Python_na_start_Kurs_video_Tworz_gry_w_PyGame/img/6.png',]
cub_numer = random.randint(0, 5)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                cub_numer = random.randint(0, 5)
                
    image = pygame.image.load(file_list[cub_numer])
    WIN.blit(image, (5, 5))
                  

    pygame.display.update()


