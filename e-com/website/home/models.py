from django.db import models

# Create your models here.

class prod(models.Model):
    name  = models.CharField(max_length=200, unique= True)
    deisc = models.CharField(max_length=200, unique= False)
    price = models.IntegerField(default=10)
    thumbnail = models.URLField(default="https://cdn.pixabay.com/photo/2016/10/06/19/59/sign-1719892_1280.png")

    def __str__(self):
        return self.name