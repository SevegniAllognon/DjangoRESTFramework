from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField("Name", max_length=500)
    email = models.EmailField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name