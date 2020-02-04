# -*- coding: utf-8 -*-
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from .models import Categoria, Dicho
from django.conf import settings


class CategoriaSerializer(ModelSerializer):

    class Meta:
        model = Categoria
        fields = (
            'id', 'nombre'
        )

class DichoSerializer(ModelSerializer):
    
    categoria = CategoriaSerializer(many=True)
    
    class Meta:
        model = Dicho
        fields = (
            'id', 'titulo', 'dicho', 'fecha_creacion', 'categoria', 'rango'
        )