from django.db import models

class Storage(models.Model):
    name = models.CharField(max_length=255, unique=True)
    amount = models.IntegerField()

    def __str__(self):
        return f'{self.name}'