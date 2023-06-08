from django.db import models


class Party(models.Model):
    title = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    category = models.CharField(max_length=24)
    place = models.CharField(max_length=255)
    member_limit = models.IntegerField()
    now_member = models.IntegerField(default = 1, null = True)
    date = models.DateTimeField()
    description = models.TextField(blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()