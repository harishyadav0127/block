from django.db import models

class Block(models.Model):
    description = models.TextField()

    def __str__(self):
        return self.description