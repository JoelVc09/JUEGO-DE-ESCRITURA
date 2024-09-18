import pygame
from Personaje import Cubo 
from Enemigo import *

import random

pygame.init()

ANCHO = 1000
ALTO = 800
VENTANA = pygame.display.set_mode([ANCHO, ALTO])
pygame.display.set_caption("Ventana de Pygame")
FPS = 60 

jugando = True 
cubo = Cubo(100,100)
reloj = pygame.time.Clock()
tiempo_pasado = 0
tiempo_entre_enemigos= 500
enemigos = []


def gestionar_teclas(teclas):
    if   teclas[pygame.K_w]:
        cubo.y -= cubo.velocidad
    if   teclas[pygame.K_s]:
        cubo.y += cubo.velocidad
    if   teclas[pygame.K_a]:
        cubo.x -= cubo.velocidad
    if   teclas[pygame.K_d]:
        cubo.x += cubo.velocidad

while jugando:
    
    tiempo_pasado += reloj.tick(FPS)
    
    if tiempo_pasado > tiempo_entre_enemigos:
        enemigos.append(Enemigo(random.randint(0,ANCHO),-50))
        tiempo_pasado = 0 
    
    eventos = pygame.event.get()
    teclas = pygame.key.get_pressed()
    
    gestionar_teclas(teclas)
    
    for evento in eventos:

        if evento.type == pygame.QUIT:
            jugando = False
    VENTANA.fill("Black")    
    cubo.dibujar(VENTANA)
    
    for enemigo in enemigos:
        enemigo.dibujar(VENTANA)
        enemigo.movimiento()
    # Aquí podrías agregar actualizaciones de pantalla si es necesario
    pygame.display.update()

pygame.quit()
