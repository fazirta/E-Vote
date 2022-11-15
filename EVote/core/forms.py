from django import forms
from . import models

class Voting(forms):
    class Meta:
        model=models.Voting
        fields=['paslon_1', 'paslon_2', 'paslon_3', 'paslon_4']

#def ny gangerti lg