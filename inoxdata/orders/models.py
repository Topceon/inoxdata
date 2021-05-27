from django.db import models


class Orders(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    otk = models.BooleanField()
    part = models.ForeignKey('Parts', on_delete=models.PROTECT)


class Parts(models.Model):
    title = models.CharField(max_length=255)
    content = models.IntegerField(max_length=255)
