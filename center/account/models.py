from django.db import models

# Create your models here.

class UserProfile(models.Model):

    name = models.CharField(max_length = 50, null = True)

    lastname = models.CharField(max_length = 50, null = True)

    city = models.CharField(max_length = 50, null = True)

    zipcode = models.CharField(max_length = 6, null = True)

    division = models.CharField(max_length = 50, null = True)

    profile_picture = models.ImageField( upload_to = 'images/')

    def __str__(self):

        return self.name



