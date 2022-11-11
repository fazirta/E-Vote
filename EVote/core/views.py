from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect
from . import models

def voting_view(request):
    contexts = {}
    return render(request, 'core/voting.html', contexts)

def success_view(request):
    contexts = {}
    return render(request, 'core/success.html', contexts)