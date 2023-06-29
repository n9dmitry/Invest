from django.db import models

class Ad(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='static/', blank=True)
    description = models.TextField(max_length=1000)


    def __str__(self):
        return self.title