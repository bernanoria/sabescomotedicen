# -*- coding: utf-8 -*-
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from .models import Categoria, Dicho
from django.conf import settings


class CategoriaSerializer(ModelSerializer):

    class Meta:
        model = Categoria
        fields = ('nombre',)

class DichoSerializer(ModelSerializer):
    
    categoria = CategoriaSerializer(many=True)
    
    class Meta:
        model = Dicho
        fields = (
            'titulo', 'dicho', 'categoria', 'rango'
        )