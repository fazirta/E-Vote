from django.db import models

# Create your models here.

class Voting(models.Model):
    Paslon_1 = models.PositiveIntegerField(default=0)
    Paslon_2 = models.PositiveIntegerField(default=0)
    paslon_3 = models.PositiveIntegerField(default=0)
    paslon_4 = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.Paslon_1