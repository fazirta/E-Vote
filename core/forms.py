from django import forms
from . import models
from django.forms import ModelForm

class VotingForm(ModelForm):
    class Meta:
        model = models.Voting
        fields = ['candidate']

    def __init__(self, *args, **kwargs):
        super(VotingForm, self).__init__(*args, **kwargs)
        self.fields['candidate'].widget.attrs.update(
            {'placeholder': 'Candidate'})

#def ny gangerti lg