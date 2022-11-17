from django.db import models

# Create your models here.

class Candidate(models.Model):
    nama_paslon = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nama_paslon

class Vote(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)

    def __str__(self):
        return self.candidate.nama_paslon