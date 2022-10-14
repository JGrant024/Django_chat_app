from django.db import models
from django.db import models
from django.conf import settings
# Create your models here.


class Room(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    image = models.ImageField(upload_to="Room", null=True)

    def __str__(self):
        return self.title

# update text book and author 
class Message(models.Model):
    text = models.TextField()
    book = models.ForeignKey(Room, on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.text[:50]
