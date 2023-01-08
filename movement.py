import pygame
from options import *
from threading import Thread
import time
import keyboard

def player1():
    # player 1
    if (settings.keys[pygame.K_a] and p1.x >settings.radius) and (p1.x > p2.x + settings.radius * 2 or p1.y < p2.y - settings.radius or p1.y > p2.y + settings.radius or p1.x < p2.x+settings.radius):
        p1.x -= settings.vel
        p1.coordinate = [p1.x, p1.y]
    if (settings.keys[pygame.K_d] and p1.x < settings.screen_width - settings.radius) and (p1.x < p2.x - settings.radius * 2 or p1.y > p2.y + settings.radius or p1.y < p2.y - settings.radius or p1.x > p2.x-settings.radius):
        p1.x += settings.vel
        p1.coordinate = [p1.x, p1.y]
    if (settings.keys[pygame.K_w] and p1.y >settings.radius) and (p1.y > p2.y + settings.radius * 2 or p1.x < p2.x - settings.radius or p1.x > p2.x + settings.radius or p1.y < p2.y-settings.radius):
        p1.y -= settings.vel
        p1.coordinate = [p1.x, p1.y]
    if (settings.keys[pygame.K_s] and p1.y < settings.screen_height - settings.radius) and (p1.y < p2.y - settings.radius * 2 or p1.x > p2.x + settings.radius or p1.x < p2.x - settings.radius or p1.y > p2.y+settings.radius):
        p1.y += settings.vel
        p1.coordinate = [p1.x, p1.y]


def player2():
    # player 2
    if (settings.keys[pygame.K_LEFT] and p2.x >settings.radius) and (p2.x > p1.x + settings.radius * 2 or p2.y < p1.y - settings.radius or p2.y > p1.y + settings.radius or p2.x < p1.x+settings.radius):
        p2.x -= settings.vel
        p2.coordinate = [p2.x, p2.y]
    if (settings.keys[pygame.K_RIGHT] and p2.x < settings.screen_width - settings.radius) and (p2.x < p1.x - settings.radius * 2 or p2.y > p1.y + settings.radius or p2.y < p1.y - settings.radius or p2.x > p1.x-settings.radius):
        p2.x += settings.vel
        p2.coordinate = [p2.x, p2.y]
    if (settings.keys[pygame.K_UP] and p2.y >settings.radius) and (p2.y > p1.y + settings.radius * 2 or p2.x < p1.x - settings.radius or p2.x > p1.x + settings.radius or p2.y < p1.y-settings.radius):
        p2.y -= settings.vel
        p2.coordinate = [p2.x, p2.y]
    if (settings.keys[pygame.K_DOWN] and p2.y < settings.screen_height - settings.radius) and (p2.y < p1.y - settings.radius * 2 or p2.x > p1.x + settings.radius or p2.x < p1.x - settings.radius or p2.y > p1.y+settings.radius):
        p2.y += settings.vel
        p2.coordinate = [p2.x, p2.y]


def strings1():
    while True:
        if settings.keys[pygame.K_r]:
            if p1.string:
                p1.string = False
                time.sleep(0.3)
            else:
                p1.string = True
                time.sleep(0.3)

def strings2():
    while True:
        if settings.keys[pygame.K_RSHIFT]:
            if p2.string:
                p2.string = False
                time.sleep(0.3)
            else:
                p2.string = True
                time.sleep(0.3)

def controls():
    player1(), player2()