from django.db import models

class Party(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="uploads/")
    category = models.CharField(max_length=24)
    place = models.CharField(max_length=255)
    member_limit = models.IntegerField()
    date = models.DateTimeField()
    description = models.TextField(blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()