from django.db import models

# Create your models here.

class Currency(models.Model):
    cur = models.CharField(max_length=3, unique=True)


    def __str__(self):
        return self.cur
