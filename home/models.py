from django.db import models

# Create your models here.


class Clients(models.Model):

    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=11)

    def __str__(self):
        return f'{self.name} - {self.email} - {self.phone}'
