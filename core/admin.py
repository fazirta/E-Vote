from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Candidate)
@admin.register(models.Vote)
class VoteAdmin(admin.ModelAdmin):
    pass