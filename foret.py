#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import numpy as np

class Cell:
    VIDE = 0
    ARBRE = 1
    FEU = 2
    CENDRE = 3

    def __init__(self, r, c, p=0.5, etat=None):
        self.r = r
        self.c = c
        if etat is None :
            if random.random() < p :
                self.etat = Cell.ARBRE
            else :
                self.etat = Cell.VIDE
        self.next_etat = None

    def __repr__(self):
        return str(self.etat)

    def calc_next(self, voisins = None):
        self.next_etat = self.etat
        if self.etat == Cell.CENDRE:
            self.next_etat = Cell.VIDE
        elif self.etat == Cell.FEU:
            self.next_etat = Cell.CENDRE
        elif self.etat == Cell.ARBRE:
            for v in voisins:
                if v.etat == Cell.FEU:
                    self.next_etat = Cell.FEU

    def set_next(self):
        self.etat = self.next_etat

class Foret:
    def __init__(self, w, h, p=0.5):
        self.w = w
        self.h = h

        self.grille = {}
        for r in range(self.h) :
            for c in range(self.w) :
                self.grille[(r, c)] = Cell(r, c, p=p)

    def feu_alea(self):
        while True :
            c, r = random.randint(0, self.w-1), random.randint(0, self.h-1)
            if self.grille[(r, c)].etat == Cell.ARBRE :
                break
        self.grille[(r, c)].etat = Cell.FEU

    def show(self):
        for r in range(self.h) :
            for c in range(self.w) :
                print self.grille[(r, c)],
            print
        print

    def get_voisins(self, cell):
        voisins = [(-1, -1), (-1, 0), (-1, 1),
                   (0, -1),           (0, 1),
                   (1, -1),  (1, 0),  (1, 1)]

        out = []

        for vr, vc in voisins :
            r = cell.r + vr
            c = cell.c + vc
            if 0 <= r < self.h and 0 <= c < self.w :
                out.append(self.grille[(r, c)])
        return out

    def next(self):
        for cell in self.grille.values() :
            cell.calc_next(self.get_voisins(cell))
        for cell in self.grille.values() :
            cell.set_next()

if __name__ == "__main__":
    foret = Foret(20, 20)
    foret.show()
    foret.feu_alea()
    foret.show()
    foret.next()
    foret.show()
    foret.next()
    foret.show()
