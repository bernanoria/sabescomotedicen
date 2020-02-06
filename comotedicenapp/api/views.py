# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Categoria, Dicho
from .serializers import CategoriaSerializer, DichoSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpResponseRedirect, HttpResponse
import  json
from django.core import serializers
from django.core.mail import send_mail
from django.conf import settings
from django.core.files import File  # you need this somewhere
import urllib
import re
from rest_framework.generics import ListAPIView, RetrieveAPIView
import random


class CategoriaViewSet(ModelViewSet):
    http_method_names = ['get']

    def list(self, request):
        categorias = Categoria.objects.all()
        data = []
        for categoria in categorias:
            categoria_serializado = CategoriaSerializer(categoria).data
            data.append(categoria_serializado)
        
        print data
        return HttpResponse(json.dumps({"mensaje": data}), status=status.HTTP_200_OK,content_type="application/json")

    
    def retrieve(self, request, pk=None):
        categoria = Categoria.objects.get(id=pk)
        categoria_serializada = CategoriaSerializer(categoria).data
        return HttpResponse(json.dumps({"mensaje": categoria_serializada}), status=status.HTTP_200_OK,content_type="application/json")


class DichoViewSet(ModelViewSet):
    http_method_names = ['get']

    def list(self, request):
        dichos = Dicho.objects.all()
        data = []
        for dicho in dichos:
            dicho_serializado = DichoSerializer(dicho).data
            data.append(dicho_serializado)
        
        return HttpResponse(json.dumps({"mensaje": data}), status=status.HTTP_200_OK,content_type="application/json")

    def retrieve(self, request, pk=None):
        dicho = Dicho.objects.get(id=pk)
        dicho_serializado = DichoSerializer(dicho).data
        return HttpResponse(json.dumps({"mensaje": dicho_serializado}), status=status.HTTP_200_OK,content_type="application/json")


def GetDicho(ModelViewSet):
    http_method_names = ['get']

    dichos = Dicho.objects.all()
    large = len(dichos)
    elem = random.randrange(large)
    dicho_serializado = DichoSerializer(dichos[elem]).data
    return HttpResponse(json.dumps({"mensaje": dicho_serializado}), status=status.HTTP_200_OK,content_type="application/json")
