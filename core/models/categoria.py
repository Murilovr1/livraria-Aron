from django.db import models

class categoria(models.Model):
    descrição = models.CharField(max_length=100)

    ...
    def __str__(self):
        return self.descrição   