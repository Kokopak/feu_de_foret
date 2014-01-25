#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import time
import sys
import pygame
from pygame.locals import *

import foret

SIZE_CELL = 16
W = 80
H = 64


class Gui:
    def __init__(self, step_by_step=False):
        pygame.init()

        flags = DOUBLEBUF
        self.screen = pygame.display.set_mode((W * SIZE_CELL , H * SIZE_CELL), flags)
        self.screen.set_alpha(None)
        pygame.display.set_caption("Feu")

        self.start = False
        self.step_by_step = step_by_step

        self.foret = foret.Foret(H, W, 0.45)
        self.imgs = {
                "ARBRE": pygame.transform.scale(pygame.image.load("arbre.png"), (SIZE_CELL, SIZE_CELL)),
                "FEU": pygame.transform.scale(pygame.image.load("feu.png"), (SIZE_CELL, SIZE_CELL)),
                "CENDRE": pygame.transform.scale(pygame.image.load("cendre.png"), (SIZE_CELL, SIZE_CELL)),
        }

    def draw(self):
        color = None
        for (r, c), cell in self.foret.grille.items():
            pygame.draw.rect(self.screen, pygame.Color(0, 0, 0), pygame.Rect(r * SIZE_CELL, c * SIZE_CELL, SIZE_CELL, SIZE_CELL))
            if cell.etat == foret.Cell.ARBRE:
                img = self.imgs["ARBRE"]
                self.screen.blit(img, (r * SIZE_CELL, c * SIZE_CELL))
            elif cell.etat == foret.Cell.FEU:
                img = self.imgs["FEU"]
                self.screen.blit(img, (r * SIZE_CELL, c * SIZE_CELL))
            elif cell.etat == foret.Cell.CENDRE:
                img = self.imgs["CENDRE"]
                self.screen.blit(img, (r * SIZE_CELL, c * SIZE_CELL))
            else:
                pygame.draw.rect(self.screen, pygame.Color(0, 0, 0), pygame.Rect(r * SIZE_CELL, c * SIZE_CELL, SIZE_CELL, SIZE_CELL))

        pygame.display.update()

    def mainLoop(self):
        ok = True
        self.draw()
        while ok:
            for event in pygame.event.get():
                if event.type == QUIT:
                    ok = False
                elif event.type == KEYDOWN and event.key == pygame.K_SPACE:
                    if self.step_by_step:
                        self.foret.next()
                        self.draw()
                elif event.type == MOUSEBUTTONDOWN:
                    if not self.start :
                        self.start = True
                        mc, mr = pygame.mouse.get_pos()
                        mc, mr = mc / SIZE_CELL, mr / SIZE_CELL
                        self.foret.grille[(mc, mr)].etat = foret.Cell.FEU
            if not self.step_by_step:
                self.foret.next()
                self.draw()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == "--step":
            gui = Gui(step_by_step=True)
            gui.mainLoop()
    else:
        gui = Gui()
        gui.mainLoop()

