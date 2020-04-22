from django.db import models

# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=50)
    obj = models.Manager()

    def __str__(self):
        return self.name
    