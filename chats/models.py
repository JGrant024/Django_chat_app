from django.db import models
from django.db import models
from django.conf import settings
# Create your models here.


class Chat(models.Model):
    room = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    image = models.ImageField(upload_to="Chat", null=True)

    def __str__(self):
        return self.title

# update text book and author


class Message(models.Model):
    text = models.TextField()
    user = models.ForeignKey(Chat, on_delete=models.CASCADE)
    admin = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.text[:50]
