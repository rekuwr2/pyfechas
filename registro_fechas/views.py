# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpRequest
from registro_fechas.models import RegistroFechas


def new(request):
    if request.method == 'GET':
        return render(request, 'new.html')
    elif request.method == 'POST':
        registro = RegistroFechas()
        registro.nombre = request.POST.get('nombre', '')
        registro.save()
        return redirect('home')


def home(request):
    return render(request, 'home.html')