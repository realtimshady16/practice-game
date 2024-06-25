#game.py
import pygame
import sys
import random

pygame.init()

HEIGHT, WIDTH = 520, 480
pygame.display.set_caption("platformer game")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class Entity:
    def __init__(self, colour, x, y, width, height, vel=0):
        self.colour = colour
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel


def main():
    run = True
    player = Entity("white", 320, 240, 20, 20, 0.5)
    obstacle = Entity("green", random.randint(0, (WIDTH-20)), random.randint(0, (HEIGHT-20)), 20, 20, 2)
    obstacles = []
    bullet = Entity("yellow", player.x, player.y, 5, 5, 2)

    while run:
        if bullet.y < 0:
            bullet.y = player.y
            bullet.x = player.x
        #bullet = Entity("yellow", player.x, player.y, 5, 5, 2)
        #while len(obstacles) < 6:
            #obstacles.append(obstacle)
            #obstacle = Entity("green", random.randint(0, WIDTH), random.randint(0, HEIGHT), 20, 20, 2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        bullet = Entity("yellow", bullet.x, bullet.y, 5, 5, 2)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x >= 0:
            player.x -= player.vel
        if keys[pygame.K_RIGHT] and player.x <= (WIDTH - player.width):
            player.x += player.vel
        if keys[pygame.K_UP] and player.y >= 0:
            player.y -= player.vel
        if keys[pygame.K_DOWN] and player.y <= (HEIGHT - player.height):
            player.y += player.vel
        if keys[pygame.K_a]:
            bullet.y -= bullet.vel

        screen.fill("black")
        pygame.draw.rect(screen, player.colour, (player.x, player.y, player.width, player.height)) #first argument is where, second argument is colour, next argument is rectangle drawing (from x to y to width to height)
        pygame.draw.rect(screen, bullet.colour, (bullet.x, bullet.y, bullet.width, bullet.height))
        #for obstacle in obstacles:
            #if player.x == (obstacle.x+obstacle.width) or player.y == (obstacle.y+obstacle.height) or (player.x+player.width) == obstacle.x or (player.y+player.height) == obstacle.y:
            #    obstacles.remove(obstacle)
            #pygame.draw.rect(screen, obstacle.colour, (obstacle.x, obstacle.y, obstacle.width, obstacle.height))
        pygame.display.update()
    
main()