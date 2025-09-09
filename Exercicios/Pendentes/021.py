#Faça um programa que abra e reproduza o audio de um arquivo MP3
#Estudar uma video aula sobre o pygames
import pygame
import sys

pygame.init()
pygame.mixer.init()

tela = 800, 600
preto = 0, 0, 0

tela = pygame.display.set_mode((tela), 0, 12)
pygame.display.set_caption("Até que durou")

imagem = pygame.image.load(r"C:\Users\Pichau\Documents\VSCode\Python\Curso_Em_Video\Exercicios\audio, imagens e videos\Villager.png")
imagem = pygame.transform.scale(imagem, (800, 600))

som = pygame.mixer_music.load(r"C:\Users\Pichau\Documents\VSCode\Python\Curso_Em_Video\Exercicios\audio, imagens e videos\Até que durou - som.mp3")
pygame.mixer_music.play()

pygame.mixer_music.set_volume(0.5)

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    tela.fill((preto))

    tela.blit(imagem, (0, 0))

    pygame.display.flip()
