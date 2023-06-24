from django.db import models

class Ads(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='static/', blank=True)