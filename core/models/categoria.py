from django.db import models

class categoria(models.Model):
    descrição = models.CharField(max_length=100)