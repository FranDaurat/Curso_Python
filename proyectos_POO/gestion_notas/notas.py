#!/usr/bin/python3 

class Nota:

    def __init__(self, contenido):
        self.contenido = contenido

    def __str__(self):
        return self.contenido
    
    def coincide(self, texto_busqueda):
        return texto_busqueda in self.contenido