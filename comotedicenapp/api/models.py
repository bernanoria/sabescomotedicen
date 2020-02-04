# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Categoria(models.Model):
    nombre = models.TextField(unique=True)

    def __str__(self):
        return "{}".format(self.nombre)

class Dicho(models.Model):
    titulo = models.TextField(unique=True)
    dicho = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    categoria = models.ManyToManyField(Categoria)
    rango = models.FloatField()

    def __str__(self):
        return "{}".format(self.titulo)
