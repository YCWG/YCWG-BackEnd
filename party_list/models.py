from django.db import models


class Party(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=24)
    place = models.CharField(max_length=255)
    member_limit = models.IntegerField(default = 0)
    now_member = models.IntegerField(default = 1)
    date = models.CharField(max_length=28, null = True)
    image = models.ImageField(upload_to='', null = True)
    description = models.TextField(blank=True)
    latitude = models.FloatField(null = True)
    longitude = models.FloatField(null = True)
    
    def __str__(self):
        return self.title