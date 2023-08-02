from django.db import models

# Create your models here.

class Kategoria(models.Model):

    nazwa = models.CharField(max_length = 250, db_index = True)

    obraz = models.ImageField(upload_to = 'images/')

class Przedmiot(models.Model):

    opis = models.CharField(max_length = 250)