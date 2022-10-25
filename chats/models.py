from django.db import models
from django.db import models


class Channel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Message(models.Model):
    text = models.TextField()
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.text[:50]
