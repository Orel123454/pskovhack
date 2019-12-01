from django.db import models

class Person(models.Model):
    name = models.CharField(max_length = 25)
    title = models.CharField(max_length =25)
    inn = models.IntegerField()
    telefon = models.IntegerField()
    selector = models.CharField(max_length = 25)
    