from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
