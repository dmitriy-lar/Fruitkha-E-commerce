from django.db import models


class Newsletter(models.Model):
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.email


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
