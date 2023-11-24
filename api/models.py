from django.db import models


class Countries(models):
    title = models.CharField(max_length=50, verbose_name="Country Name")
    body = models.CharField(max_length=500, verbose_name="Description")
    created = models.DateTimeField(verbose_name="Created Date")
    image = models.ImageField(verbose_name="Image")

    def __str__(self):
        return self.title


class Places(models):
    title = models.CharField(max_length=50, verbose_name="Place Name")
    description = models.CharField(max_length=500, verbose_name="Description")
    created = models.DateTimeField(verbose_name="Created Date")
    image = models.ImageField(verbose_name="Image")

    def __str__(self):
        return self.title
