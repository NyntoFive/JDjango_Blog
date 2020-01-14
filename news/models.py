from django.db import models

class Headline(models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField(null=True, blank=True)
    url = models.TextField()

    def __str__(self):
        return self.title

class KnifeKit(models.Model):

    title = models.CharField(max_length=200)
    sku = models.CharField(max_length=200)
    image = models.ImageField()
    img_urls = models.CharField(max_length=500)
    description = models.TextField()
    keys = models.CharField(max_length=200)
    mdesc = models.CharField(max_length=200)

    def __str__(self):
        return self.title