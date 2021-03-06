import pygame
import math

def bind(*args) :
    pass

class DNA() :
    pass

class RNA() :
    def __init__(self) :
        self.segmented = False
        self.segment = None
    
    def translate(self, something) :
        newthing = None
        return newthing

class Protein() :
    pass

class Enzyme() :
    def __init__(self) :
        pass

    def do(self, input) :
        output = None
        return output

class Virus(pygame.sprite.DirtySprite) :
    def __init__(self) :
        pygame.sprite.DirtySprite.__init__(self)
        self.place = None
        self.similar = {}

    def enter(self, target) :
        pass

    def migrate(self, target) :
        pass

    def make(self, something) :
        pass

class Host(pygame.sprite.DirtySprite) :
    def __init__(self) :
        pygame.sprite.DirtySprite.__init__(self)
        self.symptom = []
        self.nucleus = Nucleus()
        self.cytosol = Cytosol()
        self.infected = []
        self.organ = Organ()
        self.immunity = 'Good'
        self.luck = True
        self.surface_protein = {}

    def survive(self):
        pass

    def die(self):
        pass

    def lysis(self) :
        pass

    def exocytosis(self, something) :
        pass

class Organ() :
    def __init__ (self) :
        self.sensory_nerve_ganglia = None
        self.sensory_nerve = None
        self.surface = None

class Nucleus(pygame.sprite.DirtySprite) :
    def __init__(self) :
        pygame.sprite.DirtySprite.__init__(self)
        self.gene = []
        self.anything = []

    def add_gene (self, gene : list) :
        self.gene.extend(gene)

    def add (self, something) :
        self.anything.append(something)

    def dna_polymerase (self, gene) :
        return DNA()

    def transcription_factor(self, gene) :
        return RNA()

class Cytosol(pygame.sprite.DirtySprite) :
    def __init__(self) :
        pygame.sprite.DirtySprite.__init__(self)

    def ribosome(self, mrna) :
        return Protein()

    def golgi(self, something) :
        pass