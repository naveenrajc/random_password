from django.db import models

# Create your models here.

class listModel(models.Model):

    item = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)
    