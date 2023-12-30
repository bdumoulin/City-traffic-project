from django.db import models


class Message(models.Model):
    content = models.CharField(max_length=255)

    def __str__(self):
        return self.content
