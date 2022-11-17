from django import forms
from . import models
from django.forms import ModelForm

class VoteForm(ModelForm):
    class Meta:
        model = models.Vote
        fields = ['candidate']

    def __init__(self, *args, **kwargs):
        super(VoteForm, self).__init__(*args, **kwargs)
        self.fields['candidate'].widget.attrs.update(
            {'placeholder': 'Candidate', 'multiple': ''})
