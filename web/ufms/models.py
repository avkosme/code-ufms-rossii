from django.db import models


# Create your models here.


class Ufms(models.Model):
    name = models.CharField(max_length=500)
    number = models.CharField(max_length=30)

    def __str__(self):
        return ' '.join((self.name, self.number))
