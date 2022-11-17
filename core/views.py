from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect
from . import models
from .forms import VoteForm
from django.db.models import Count

def Vote_view(request):
    form = VoteForm()

    if request.method == 'POST':
        form = VoteForm(request.POST, request.FILES)
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

def result_view(request):
    votes = [len(models.Vote.objects.filter(candidate__nama_paslon__contains="PASLON 1")), len(models.Vote.objects.filter(candidate__nama_paslon__contains="PASLON 2")), len(models.Vote.objects.filter(candidate__nama_paslon__contains="PASLON 3")), len(models.Vote.objects.filter(candidate__nama_paslon__contains="PASLON 4"))]
    contexts = {"votes": votes}
    return render(request, 'core/result.html', contexts)
