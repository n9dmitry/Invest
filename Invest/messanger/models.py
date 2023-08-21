from django.db import models

# Create your models here.


class Message(models.Model):
    date = models.DateField()
    text = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"Message {self.text}"
