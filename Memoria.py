import numpy as np

class Memoria:
    def __init__(self):
        self.memoria = []

    def loader(self, instruCodMaq):
        self.memoria = instruCodMaq

    def fetch(self, ProgramCounter):
        return self.memoria[ProgramCounter] #retorna o termo indicado pelo PC

