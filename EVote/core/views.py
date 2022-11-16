from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect
from . import models
from .forms import VotingForm

def voting_view(request):
    form = VotingForm()

    if request.method == 'POST':
        form = VotingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(to='success')

    contexts = {
        'form': form,
    }
    return render(request, 'core/voting.html', contexts)

def success_view(request):
    contexts = {}
    return render(request, 'core/success.html', contexts)

