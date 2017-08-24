# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import RequestContext
# Create your views here.

def index(request):                                               # funkcja zwracająca widok strony głównej
    return render(request,                                        # return - zwraca wynik i kończy działanie
    'index.html',                                                 # zwrot danych
        {'nazwa zmiennej': 'wartość zmiennej',
         'nazwa zmiennej 2': 'wartość zmiennej 2'})               # Przekazywane zmienne (klucz: wartość)

def contactPage(request):
    return