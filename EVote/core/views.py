from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect
from . import models

# CONTOH VIEWS
# def CONTOH_view(request):
#     contexts = {}
#     return render(request, 'FOLDER/CONTOH.html', contexts)