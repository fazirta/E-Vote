from django.db import models

# Create your models here.

class Candidate(models.Model):
    nama_paslon = models.CharField(max_length=200)
    
    def _str_(self):
        return self.nama_paslon

class Voting(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)