#Faça um programa que abra e reproduza o audio de um arquivo MP3
import pygame

pygame.init()

tela = pygame.display.set_mode((1200, 800), 0, 32)
pygame.display.set_caption('Tocando Musica no Pygame')
branco = (255, 255, 255)

pygame.mixer_music.load(r'C:\Users\Pichau\PycharmProjects\CursoEmVideo\Até que durou - som.mp3')
pygame.mixer_music.play()

villager = pygame.image.load(r'C:\Users\Pichau\PycharmProjects\CursoEmVideo\Villager.png')
villager = pygame.transform.scale (villager, (1200, 800))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if not pygame.mixer.music.get_busy():
        run = False

    tela.fill(branco)
    tela.blit(villager, (0, 0))
    pygame.display.update()


pygame.quit()
